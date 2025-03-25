"""
This file serves as the main execution for the entry point for my Clinical Trial API microservice
"""

from fastapi import FastAPI
#from app.api.routes import router

app = FastAPI()

#next i will write my constructor
if __name__ == "__main__" :
    print("welcome to the clinical trial micro service")
