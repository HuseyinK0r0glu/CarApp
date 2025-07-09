from sqlalchemy.orm import Session
from models.CarModel import Car
from models.DriverModel import Driver
from schemas.CarSchema import CarCreate , CarUpdate

def createCar(car_create: CarCreate, db: Session):
    db_car = Car(
        vehicle_type=car_create.vehicle_type,
        plate=car_create.plate,
        vehicle_name=car_create.vehicle_name,
        vehicle_color=car_create.vehicle_color,
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)

    if car_create.drivers : 
        for driver_data in car_create.drivers:
            db_driver = Driver(
                driver_gender=driver_data.driver_gender,
                driver_age=driver_data.driver_age,
                driver_name=driver_data.driver_name,
                vehicle_id=db_car.vehicle_id,
            )
            db.add(db_driver)
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
    car = db.query(Car).filter(Car.vehicle_id == id).first()
    if not car:
        return None
    return car

def deleteCar(id : int , db : Session):
    car = db.query(Car).filter(Car.vehicle_id == id).first()
    if not car:
        return None
    db.delete(car)
    db.commit()
    return car
