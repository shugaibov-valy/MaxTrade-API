from db import Base, session
import sqlalchemy as sq
from sqlalchemy.orm import relationship
from components.users import exc


class User(Base):
    __tablename__: str = 'users'

    id = sq.Column(sq.Integer, primary_key=True)
    email: str = sq.Column(sq.String)
    login: str = sq.Column(sq.String, unique=True)
    password: str = sq.Column(sq.String)
    is_admin: bool = sq.Column(sq.Boolean, unique=False, default=False)

    def __repr__(self):
        return self.login

    #метод для создания юзера
    @classmethod
    def create_user(cls, email: str, login: str, password: str):
        user = cls(email=email, login=login, password=password)
        session.add(user)
        session.commit()
        return user

    #метод для проверки существования пользователя, по логину ищем
    @classmethod
    def check_login(cls, login):
        user = session.query(cls).filter(cls.login == login).first()
        if not user:
            raise exc.RegLoginUserNotFound
        return user

    #метод для проверки существования пользователя, по логину и паролю ищем
    @classmethod
    def get_user(cls, login, password):
        user = session.query(cls).filter(
                cls.login == login, 
                cls.password == password).first()
        if not user:
            raise exc.AuthLoginUserNotFound
        return user

