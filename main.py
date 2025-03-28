"""
This file serves as the main execution for the entry point for my Clinical Trial API microservice
"""

from fastapi import FastAPI
from app.api.routes import router
import uvicorn

app = FastAPI()
app.include_router(router)


#next i will write my constructor
if __name__ == "__main__" :
    print("welcome to the clinical trial micro service")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)