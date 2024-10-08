import os
import streamlit as st

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(st.secrets["DB_SOURCE"],
                       pool_size=15,
                       max_overflow=20,
                       pool_timeout=30,
                       pool_pre_ping=True)

SessionLocal = sessionmaker(engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()