from sqlalchemy import Column, ForeignKey, Sequence, CheckConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP

from database import engine, Base


class Chats(Base):
    __tablename__ = 'Chats'

    chat_id = Column(Integer, Sequence('chat_id_seq'), primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())
    patient_id = Column(Integer, nullable=False)
    chat_reason = Column(String(250), nullable=False)
    feedback_score = Column(Integer, CheckConstraint('feedback_score BETWEEN 0 AND 10'))

class Appointments(Base):
    __tablename__ = 'Appointments'
    
    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_created_at = Column(TIMESTAMP, nullable=False)
    appointment_starts_at = Column(TIMESTAMP, nullable=False)
    chat_id = Column(Integer, nullable=False)
    patient_id = Column(Integer, nullable=False)
    

Base.metadata.create_all(bind=engine)