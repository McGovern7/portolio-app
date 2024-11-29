from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# Connect FastAPI Application to MySQL database

URL_DATABASE = 'mysql+pymysql://root:Dustinjohnson7@localhost:3306/Tarkov_Project'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()