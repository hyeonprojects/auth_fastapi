import datetime
import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from ..database import base


class User(base):
    __tablename__ = "users"

    sid = Column(String, primary_key=True, index=True, default=lambda: uuid.uuid4())
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    refresh_token = relationship('RefreshToken', back_populates='user')


class RefreshToken(base):
    __tablename__ = "refresh_token"

    sid = Column(String, primary_key=True, index=True, default=lambda: uuid.uuid4())
    refresh_token = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    owner_sid = Column(String, ForeignKey('users.sid'))

    user = relationship('User', back_populates='refresh_token')
