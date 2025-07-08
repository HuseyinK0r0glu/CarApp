from pydantic import BaseModel

# for updating a car 
class CarUpdate(BaseModel):
    vehicle_type : str | None = None
    plate : str | None = None
    vehicle_name : str | None = None
    vehicle_color : str | None = None 

# for creating a car
class CarCreate(BaseModel):
    vehicle_type: str
    plate: str
    vehicle_name: str
    vehicle_color: str