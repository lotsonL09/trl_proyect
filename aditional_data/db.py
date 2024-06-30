from sqlalchemy import create_engine
from pymongo import MongoClient

db_mongo=MongoClient()

client=db_mongo['TRL_PROYECT']

url_db="mysql+pymysql://root:1234@localhost:3306/trl_proyect" #modificar con el servidor

engine=create_engine(url_db)

