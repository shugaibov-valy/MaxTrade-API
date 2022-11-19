from db import Base, session
import sqlalchemy as sq
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from geocoder import coords_to_address
from components.users.model import User


class Complaint(Base):
    __tablename__: str = 'complaints'
    id = sq.Column(sq.Integer, primary_key=True)
    title: str = sq.Column(sq.String)
    longitude: float = sq.Column(sq.Float)
    latitude: float = sq.Column(sq.Float)
    address: str = sq.Column(sq.String)
    desc: str = sq.Column(sq.String)
    mess_of_minstroy: str = sq.Column(sq.String)
    category: str = sq.Column(sq.String)
    problemImageURL: str = sq.Column(sq.String)
    is_satisfied: bool = sq.Column(sq.Boolean, unique=False, default=False)
    count_like: int = sq.Column(sq.Integer, default=0)
    created_at = sq.Column(sq.DateTime, server_default=func.now())
    user_id: int  = sq.Column(sq.Integer, sq.ForeignKey('users.id'))        ### id создателя, пользователя
    user = relationship("User", foreign_keys=[user_id])

    def to_json(self):
        return {
            "title": self.title,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "streetName": self.address,
            "description": self.desc,
            "minDescription": self.mess_of_minstroy,
            "problemImageURL": self.problemImageURL,
            "type": self.category,
            "count_like": self.count_like,
            "isDecided": self.is_satisfied,
            "date": str(self.created_at)
        }


    ### получение жалобы по ее id в БД
    @classmethod
    def get_by_id(cls, comlaint_id):
        complaint = session.query(cls).filter(cls.id == comlaint_id).first()
        return complaint




    #метод для создания жалобы
    @classmethod
    def create_complaint(cls, title: str, longitude: str, latitude: str, desc: str, category: str, user_id: int, problemImageURL: str):
        complaint = cls(title=title, 
                        longitude=longitude, 
                        latitude=latitude, 
                        address=coords_to_address(longitude, latitude), 
                        desc=desc, 
                        category=category, 
                        user_id=user_id,
                        problemImageURL=problemImageURL)
        session.add(complaint)
        session.commit()
        return complaint


    #метод для выгрузки жалоб пользователя по его user_id
    @classmethod
    def comlaints_by_user_id(cls, user_id):
        comlaints = session.query(cls).filter(cls.user_id == user_id).all()
        return comlaints

    # метод для выгрузки всех жалоб
    @classmethod
    def all_comlaints(cls):
        comlaints = session.query(cls).all()
        return comlaints
        


