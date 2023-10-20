from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from core.db import Base


class User(Base):
    __tablename__ = "user_directory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    age = Column(Integer)
    gender = Column(String)
    nationality = Column(String)
    date_added = Column(DateTime, default=datetime.utcnow)
