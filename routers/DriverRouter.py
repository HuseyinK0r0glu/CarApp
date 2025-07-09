from fastapi import APIRouter , Depends , HTTPException
from fastapi.testclient import TestClient
from database import get_db
from typing import List

# for database connection
from database import Base , engine , SessionLocal
from models.DriverModel import Driver 
from sqlalchemy.orm import Session

# schemas (models) 
from schemas.DriverSchema import DriverCreate , DriverUpdate , DriverResponse

# service
from services.DriverService import getAllDrivers , createDriver , getDriver , deleteDriver , updateDriver

Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/drivers" , response_model=List[DriverResponse])
async def get_drivers(db : Session = Depends(get_db)):
    drivers = getAllDrivers(db)
    return drivers

@router.get("/driver/{id}")
async def get_driver(id : int , db : Session = Depends(get_db)):
    driver = getDriver(id,db)
    if not driver : 
        raise HTTPException(status_code=404,detail="Driver not found")

    driver_dict = {
        "driver_id" : driver.driver_id,
        "driver_gender" : driver.driver_gender,
        "driver_age": driver.driver_age,
        "driver_name": driver.driver_name,
        "vehicle": driver.vehicle
    }
    return driver_dict

@router.post("/createDriver" , response_model=DriverResponse)
async def create_driver(driver: DriverCreate, db: Session = Depends(get_db)):
    db_driver = createDriver(driver, db)
    return db_driver

@router.delete("/deleteDriver/{id}")
async def delete_driver(id : int , db : Session = Depends(get_db)):
    driver = deleteDriver(id, db)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return {"result": f"Driver with id {id} deleted successfully"}


@router.put("/updateDriver/{id}" ,response_model = DriverResponse)
async def update_driver(id: int, driver_update: DriverUpdate, db: Session = Depends(get_db)):
    driver = updateDriver(id, driver_update, db)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver