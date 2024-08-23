from sqlmodel import SQLModel, create_engine, select

import os

connecion_string = os.getenv('DB_URI')
engine = create_engine(connecion_string)

def create_tables():
    SQLModel.metadata.create_all(engine)