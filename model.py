from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PhoneNumber(Base):
    __tablename__ = 'phone_numbers'

    id = Column(Integer, primary_key=True)
    number = Column(String, unique=True, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'))

    client = relationship('Client', back_populates='phone_numbers')


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url_planfix = Column(String)
    token_planfix = Column(String)
    name_session = Column(String)
    path_session = Column(String)

    phone_numbers = relationship('PhoneNumber', back_populates='client')

    work = relationship('WorkClient', uselist=False, back_populates='client')

class WorkClient(Base):
    __tablename__ = 'work_clients'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    phone_number_id = Column(Integer, ForeignKey('phone_numbers.id'))
    status = Column(String)
    token = Column(String)
    error = Column(String)

    client = relationship('Client', back_populates='work')
    phone_number = relationship('PhoneNumber')


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    cmd = Column(String)
    provider_id = Column(String)
    chat_id = Column(String)
    token = Column(String)
    message = Column(String)
    message_id = Column(String)
    user_name = Column(String)
    user_last_name = Column(String)
    user_ico = Column(String)
    task_email = Column(String)
    contact_phone = Column(String)
    channel = Column(String)
    telegram_user_name = Column(String)
    telegram_user_id = Column(String)
    attachment_url = Column(String)
    attachment_name = Column(String)