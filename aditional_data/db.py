from sqlalchemy import create_engine

url_db="mysql+pymysql://root:Hola.12345@localhost:3306/trl_proyect" #modificar con el servidor

engine=create_engine(url_db)

