from sqlalchemy import Column , String , Integer , ForeignKey 
from database import Base
from sqlalchemy.orm import relationship   

class Driver(Base):
    __tablename__ = "drivers"
    driver_id = Column(Integer,primary_key=True,autoincrement=True)
    driver_gender = Column(String)
    driver_age = Column(String)
    driver_name = Column(String)

    vehicle_id = Column(Integer,ForeignKey("cars.vehicle_id"))
    vehicle = relationship("Car" , back_populates="drivers")