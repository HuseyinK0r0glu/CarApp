from pydantic import BaseModel

# for updating a driver 
class DriverUpdate(BaseModel):
    driver_age : str | None = None
    driver_name : str | None = None
    drivers_cars_plate : str | None = None 

# for creating a driver
class DriverCreate(BaseModel):
    driver_gender : str
    driver_age: str
    driver_name: str
    drivers_cars_plate: str


class DriverResponse(BaseModel):
    driver_id: int
    driver_gender: str
    driver_age: str
    driver_name: str
    drivers_cars_plate: str

    class Config:
        orm_mode = True