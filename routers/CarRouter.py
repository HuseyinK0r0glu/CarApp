from fastapi import APIRouter , Depends , HTTPException
from fastapi.testclient import TestClient
from database import get_db

# for database connection
from database import Base , engine , SessionLocal
from models.CarModel import Car
from sqlalchemy.orm import Session

# schemas (models) 
from schemas.CarSchema import CarUpdate , CarCreate

# service
from services.CarService import getAllCars , getCar , deleteCar , createCar , updateCar

# TODO : write a method for creating a JSON

Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/")
async def firstApiCall():
    return {"message" : "Hello World"}

@router.post("/createCar")
async def create_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = createCar(car, db)
    return {
        "vehicle_type": db_car.vehicle_type,
        "plate": db_car.plate,
        "vehicle_name": db_car.vehicle_name,
        "vehicle_color": db_car.vehicle_color,
    }

@router.get("/car/{id}")
async def get_car(id : int , db : Session = Depends(get_db)):
    car = getCar(id,db)
    if not car : 
        raise HTTPException(status_code=404,detail="Car not found")
    car_dict = {
        "vehicle_id" : car.vehicle_id,
        "vehicle-type" : car.vehicle_type,
        "plate": car.plate,
        "vehicle_name": car.vehicle_name,
        "vehicle_color": car.vehicle_color,
    }
    return car_dict

@router.get("/cars")
async def get_cars(db : Session = Depends(get_db)):
    cars = getAllCars(db)
    # to convert to JSON
    result = []
    for car in cars : 
        car_dict = {
            "vehicle_id" : car.vehicle_id,
            "vehicle-type" : car.vehicle_type,
            "plate": car.plate,
            "vehicle_name": car.vehicle_name,
            "vehicle_color": car.vehicle_color,
        }
        result.append(car_dict)
    return result

@router.delete("/delete/{id}")
async def delete_car(id : int , db : Session = Depends(get_db)):
    car = deleteCar(id, db)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return {"result": f"Car with id {id} deleted successfully"}

@router.put("/update/{id}")
async def update_car(id: int, car_update: CarUpdate, db: Session = Depends(get_db)):
    car = updateCar(id, car_update, db)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return {
        "vehicle_id": car.vehicle_id,
        "vehicle_type": car.vehicle_type,
        "plate": car.plate,
        "vehicle_name": car.vehicle_name,
        "vehicle_color": car.vehicle_color,
    }
