from sqlalchemy import Column , String , Integer , Enum
from database import Base
from enums.carEnums import FuelType
from sqlalchemy.orm import relationship

class Car(Base):
    __tablename__ = "cars"
    vehicle_id = Column(Integer,primary_key=True,autoincrement=True)
    vehicle_type = Column(String,index=True)
    plate = Column(String)
    vehicle_name = Column(String)
    vehicle_color = Column(String)
    fuel_type = Column(Enum(FuelType) , nullable=True)

    # One to many relationship
    drivers = relationship("Driver",back_populates="vehicle")
