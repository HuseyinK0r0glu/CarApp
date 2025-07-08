from sqlalchemy.orm import Session
from models.DriverModel import Driver

from schemas.DriverSchema import DriverCreate , DriverUpdate

def getAllDrivers(db : Session):
    return db.query(Driver).all()

def getDriver(id : int , db : Session):
    return db.query(Driver).filter(Driver.driver_id == id).first()

def createDriver(driver_create: DriverCreate, db: Session):
    db_driver = Driver(**driver_create.dict())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

def deleteDriver(id : int , db : Session):
    driver = db.query(Driver).filter(Driver.driver_id == id).first()
    if not driver:
        return None
    db.delete(driver)
    db.commit()
    return driver

def updateDriver(id: int, driver_update: DriverUpdate, db: Session):
    driver = db.query(Driver).filter(Driver.driver_id == id).first()
    if not driver:
        return None
    updated_data = driver_update.dict(exclude_unset=True)
    for key, value in updated_data.items():
        setattr(driver, key, value)
    db.commit()
    db.refresh(driver)
    return driver