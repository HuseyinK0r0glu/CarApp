from fastapi import FastAPI
from typing import List

from routers import CarRouter,DriverRouter

# responses from schemas 
from schemas.DriverSchema import DriverResponse

app = FastAPI()

# endpoints for vehicle
app.add_api_route("/firstApiCall",CarRouter.firstApiCall,methods=["GET"])
app.add_api_route("/createCar",CarRouter.create_car,methods=["POST"])
app.add_api_route("/car/{id}",CarRouter.get_car, methods=["GET"])
app.add_api_route("/cars", CarRouter.get_cars, methods=["GET"])
app.add_api_route("/deleteCar/{id}", CarRouter.delete_car, methods=["DELETE"])
app.add_api_route("/updateCar/{id}", CarRouter.update_car, methods=["PUT"])

# endppints for driver
app.add_api_route("/drivers",DriverRouter.get_drivers,methods=["GET"],response_model=List[DriverResponse])
app.add_api_route("/driver/{id}",DriverRouter.get_driver,methods=["GET"])
app.add_api_route("/createDriver",DriverRouter.create_driver,methods=["POST"],response_model=DriverResponse)
app.add_api_route("/deleteDriver/{id}",DriverRouter.delete_driver,methods=["DELETE"])
app.add_api_route("/updateDriver/{id}",DriverRouter.update_driver,methods=["PUT"],response_model = DriverResponse)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)