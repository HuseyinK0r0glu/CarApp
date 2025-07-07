from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
async def firstApiCall():
    return {"message" : "Hello World"}