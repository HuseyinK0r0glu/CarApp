from sqlalchemy import Column , String , Integer 
from database import Base

# TODO : one-to-one or one-to-many relationship could be added 

class Driver(Base):
    __tablename__ = "drivers"
    driver_id = Column(Integer,primary_key=True,autoincrement=True)
    driver_gender = Column(String)
    driver_age = Column(String)
    driver_name = Column(String)
    drivers_cars_plate = Column(String)