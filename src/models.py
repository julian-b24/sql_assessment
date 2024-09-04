from sqlalchemy import Column, ForeignKey, Sequence
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

from src.database import engine, Base


class Chats(Base):
    __tablename__ = 'Chats'

    chat_id = Column(Integer, Sequence('chat_id_seq'), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    patient_id = Column(Integer, nullable=False)
    chat_reason = Column(String(250), nullable=False)
    feedback_score = Column(Integer, nullable=False)


class Appointments(Base):
    __tablename__ = 'Appointments'
    
    appointment_id = Column(Integer, Sequence('appointment_id_seq'), primary_key=True)
    appointment_created_at = Column(DateTime, nullable=False, default=func.now())
    appointment_starts_at = Column(DateTime, nullable=False)
    chat_id = Column(Integer, ForeignKey(''))
    patient_id = Column(Integer, nullable=False)

    chat = relationship("Chats", foreign_keys=chat_id, overlaps="Chats")


Base.metadata.create_all(bind=engine)