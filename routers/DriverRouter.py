from fastapi import APIRouter , Depends , HTTPException
from fastapi.testclient import TestClient
from database import get_db

# for database connection
from database import Base , engine , SessionLocal
from models.DriverModel import Driver 
from sqlalchemy.orm import Session

# schemas (models) 
from schemas.DriverSchema import DriverCreate , DriverUpdate

# service
from services.DriverService import getAllDrivers , createDriver , getDriver , deleteDriver , updateDriver

# TODO : write a method for creating a JSON

Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/drivers")
async def get_drivers(db : Session = Depends(get_db)):
    drivers = getAllDrivers(db)
    # to convert to JSON
    result = []
    for driver in drivers : 
        driver_dict = {
            "driver_id" : driver.driver_id,
            "driver_gender" : driver.driver_gender,
            "driver_age": driver.driver_age,
            "driver_name": driver.driver_name,
            "drivers_cars_plate": driver.drivers_cars_plate,
        }
        result.append(driver_dict)
    return result

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
        "drivers_cars_plate": driver.drivers_cars_plate,
    }
    return driver_dict

@router.post("/createDriver")
async def create_driver(driver: DriverCreate, db: Session = Depends(get_db)):
    db_driver = createDriver(driver, db)
    return {
        "driver_gender" : db_driver.driver_gender,
        "driver_age": db_driver.driver_age,
        "driver_name": db_driver.driver_name,
        "drivers_cars_plate": db_driver.drivers_cars_plate,
    }

@router.delete("/deleteDriver/{id}")
async def delete_driver(id : int , db : Session = Depends(get_db)):
    driver = deleteDriver(id, db)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return {"result": f"Driver with id {id} deleted successfully"}


@router.put("/updateDriver/{id}")
async def update_driver(id: int, driver_update: DriverUpdate, db: Session = Depends(get_db)):
    driver = updateDriver(id, driver_update, db)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return {
        "driver_id" : driver.driver_id,
        "driver_gender" : driver.driver_gender,
        "driver_age": driver.driver_age,
        "driver_name": driver.driver_name,
        "drivers_cars_plate": driver.drivers_cars_plate,
    }