from db import Base, session
import sqlalchemy as sq
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from geocoder import coords_to_address


class Mark(Base):
    __tablename__: str = 'marks'

    id = sq.Column(sq.Integer, primary_key=True)
    longitude: float = sq.Column(sq.Float)
    latitude: float = sq.Column(sq.Float)
    address: str = sq.Column(sq.String)
    description: str = sq.Column(sq.String)
    date: str = sq.Column(sq.DateTime, server_default=func.now())


    def to_json(self):
        return {
            "id": self.id,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "streetName": self.address,
            "description": self.description,
            "date": str(self.date)
        }


    #метод для создания метки
    @classmethod
    def create_mark(cls, longitude: str, latitude: str, description: str):
        mark = cls(longitude=longitude, latitude=latitude, description=description, address=coords_to_address(longitude, latitude))
        session.add(mark)
        session.commit()
        return mark

    @classmethod
    def all_marks(cls):
        marks = session.query(cls).all()
        return marks

    @classmethod
    def get_by_id(cls, mark_id):
        mark = session.query(cls).filter(cls.id == mark_id).first()
        return mark


