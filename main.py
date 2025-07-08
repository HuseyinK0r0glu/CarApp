from fastapi import FastAPI
from routers.CarRouter import router as carRouter  

app = FastAPI()

app.include_router(carRouter)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)