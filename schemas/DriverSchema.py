from pydantic import BaseModel
    
# for updating a driver 
class DriverUpdate(BaseModel):
    driver_age : str | None = None
    driver_name : str | None = None

# for creating a driver
class DriverCreate(BaseModel):
    driver_gender : str
    driver_age: str
    driver_name: str

# for vehicle repsonse 
class CarResponse(BaseModel):
    vehicle_id: int
    vehicle_type: str
    plate: str
    vehicle_name: str
    vehicle_color: str
    fuel_type: str

    class Config:
        orm_mode = True

class DriverResponse(BaseModel):
    driver_id: int
    driver_gender: str
    driver_age: str
    driver_name: str
    vehicle: CarResponse | None = None

    class Config:
        orm_mode = True