from sqlalchemy.orm import Session
from models.CarModel import Car
from schemas.CarSchema import CarCreate , CarUpdate

def createCar(car_create: CarCreate, db: Session):
    db_car = Car(**car_create.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def updateCar(id: int, car_update: CarUpdate, db: Session):
    car = db.query(Car).filter(Car.vehicle_id == id).first()
    if not car:
        return None
    updated_data = car_update.dict(exclude_unset=True)
    for key, value in updated_data.items():
        setattr(car, key, value)
    db.commit()
    db.refresh(car)
    return car

def getAllCars(db : Session):
    return db.query(Car).all()

def getCar(id : int , db : Session):
    return db.query(Car).filter(Car.vehicle_id == id).first()

def deleteCar(id : int , db : Session):
    car = db.query(Car).filter(Car.vehicle_id == id).first()
    if not car:
        return None
    db.delete(car)
    db.commit()
    return car
    