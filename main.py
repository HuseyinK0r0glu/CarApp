from fastapi import FastAPI
from routers.CarRouter import router as carRouter  
from routers.DriverRouter import router as driverRouter

app = FastAPI()

app.include_router(carRouter)
app.include_router(driverRouter)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)