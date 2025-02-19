from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:Sqlzaebal@localhost/peta"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Animal(Base):  # Это модель БД, создаёт таблицу "animals"
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    age = Column(String)
    sex = Column(String)
    description = Column(String)
    photo_url = Column(String)

# Создаём таблицы в БД
Base.metadata.create_all(bind=engine)
