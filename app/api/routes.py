"""
this File serves as the fetch data and results function for the API endpoints
"""

from fastapi import APIRouter
from app.services.fetcher import Fetch_and_Store_data  #importing method from the fecher.py file in services

router = APIRouter()


@router.get("/fetch_data")
async def fetch_data():
    return await Fetch_and_Store_data()


