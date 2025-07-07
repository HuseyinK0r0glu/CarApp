from fastapi import FastAPI , Depends , HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel

# for database connection
from database import Base , engine , SessionLocal
from models import Car
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        # Yield pauses a function's execution and returns a value temporarily
        yield db
    finally:
        db.close()

@app.get("/")
async def firstApiCall():
    return {"message" : "Hello World"}

@app.post("/createCar")
async def create_car(car : dict , db : Session = Depends(get_db)):
    db_car = Car(**car)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return {
        "vehicle-type": car["vehicle_type"],
        "plate": car["plate"],
        "vehicle_name": car["vehicle_name"],
        "vehicle_color": car["vehicle_color"],
    }

@app.get("/cars")
async def get_cars(db : Session = Depends(get_db)):
    cars =db.query(Car).all()
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

@app.delete("/delete/{id}")
async def delete_car(id : int , db : Session = Depends(get_db)):
    car = db.query(Car).filter(Car.vehicle_id == id).first()
    if not car : 
        raise HTTPException(status_code=404,detail="Car not found")
    db.delete(car)
    db.commit()
    return {"result" : f"Car with id {id} deleted succesfully"}

# for updating a car 
class CarUpdate(BaseModel):
    vehicle_type : str | None = None
    plate : str | None = None
    vehicle_name : str | None = None
    vehicle_color : str | None = None 

@app.put("/update/{id}")
async def update_car(id : int , car_update : CarUpdate , db : Session = Depends(get_db)):
    car = db.query(Car).filter(Car.vehicle_id == id).first()
    if not car : 
        raise HTTPException(status_code=404,detail="Car not found")
    updated_data = car_update.dict(exclude_unset=True)
    for key , value in updated_data.items():
        setattr(car,key,value)
    db.commit()
    db.refresh(car)
    result = {
        "vehicle_id" : car.vehicle_id,
        "vehicle-type" : car.vehicle_type,
        "plate": car.plate,
        "vehicle_name": car.vehicle_name,
        "vehicle_color": car.vehicle_color,
    }
    return result
