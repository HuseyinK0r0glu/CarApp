from fastapi import Depends , HTTPException

# for database connection
from database import get_db
from database import Base , engine
from sqlalchemy.orm import Session

# schemas (models) 
from schemas.CarSchema import CarUpdate , CarCreate

# service
from services.CarService import getAllCars , getCar , deleteCar , createCar , updateCar

async def firstApiCall():
    return {"message" : "Hello World"}

async def create_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = createCar(car, db)
    return db_car

async def get_car(id : int , db : Session = Depends(get_db)):
    car = getCar(id,db)
    if not car : 
        raise HTTPException(status_code=404,detail="Car not found")
    
    drivers = []

    for driver in car.drivers:
        temp_driver = {
                "driver_id": driver.driver_id,
                "driver_gender": driver.driver_gender,
                "driver_age": driver.driver_age,
                "driver_name": driver.driver_name
            }
        drivers.append(temp_driver)

    car_dict = {
        "vehicle_id" : car.vehicle_id,
        "vehicle-type" : car.vehicle_type,
        "plate": car.plate,
        "vehicle_name": car.vehicle_name,
        "vehicle_color": car.vehicle_color,
        "fuel_type": car.fuel_type,
        "drivers" : drivers
    }
    return car_dict

async def get_cars(db : Session = Depends(get_db)):
    cars = getAllCars(db)
    # to convert to JSON
    result = []
    for car in cars : 

        drivers = []

        for driver in car.drivers:
            temp_driver = {
                    "driver_id": driver.driver_id,
                    "driver_gender": driver.driver_gender,
                    "driver_age": driver.driver_age,
                    "driver_name": driver.driver_name
                }
            drivers.append(temp_driver)

        car_dict = {
            "vehicle_id" : car.vehicle_id,
            "vehicle-type" : car.vehicle_type,
            "plate": car.plate,
            "vehicle_name": car.vehicle_name,
            "vehicle_color": car.vehicle_color,
            "drivers" : drivers,
            "fuel_type": car.fuel_type
        }
        result.append(car_dict)
    return result

async def delete_car(id : int , db : Session = Depends(get_db)):
    car = deleteCar(id, db)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    # change the fields of driver after deleting the car 
    for driver in car.drivers:
        driver.vehicle_id = None
    
    db.commit() 
    return {"result": f"Car with id {id} deleted successfully"}

async def update_car(id: int, car_update: CarUpdate, db: Session = Depends(get_db)):
    car = updateCar(id, car_update, db)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    
    drivers = []

    for driver in car.drivers:
        drivers.append(driver)

    return {
        "vehicle_id": car.vehicle_id,
        "vehicle_type": car.vehicle_type,
        "plate": car.plate,
        "vehicle_name": car.vehicle_name,
        "vehicle_color": car.vehicle_color,
        "drivers" : drivers,
        "fuel_type": car.fuel_type
    }   