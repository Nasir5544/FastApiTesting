from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine=create_engine("mysql://root:123456789@localhost:3306/fastapi")
meta= MetaData()
conection=engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()