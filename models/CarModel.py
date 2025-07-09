from sqlalchemy import Column , String , Integer 
from database import Base
from sqlalchemy.orm import relationship

class Car(Base):
    __tablename__ = "cars"
    vehicle_id = Column(Integer,primary_key=True,autoincrement=True)
    vehicle_type = Column(String,index=True)
    plate = Column(String)
    vehicle_name = Column(String)
    vehicle_color = Column(String)

    # One to many relationship
    drivers = relationship("Driver",back_populates="vehicle")
