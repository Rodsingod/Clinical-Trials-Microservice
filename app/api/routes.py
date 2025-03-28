"""
this File serves as the fetch data and results function for the API endpoints

It includes:
- /fetch_data: Fetches data from the external API and stores it.
- /results: Returns the latest stored clinical trial entries from the database.
"""

from fastapi import APIRouter
from app.services.fetcher import Fetch_and_Store_data  #importing method from the fecher.py file in services

#importing functions from the database Directory
from app.db.crud import get_trials
from app.db.session import local_Session

#this will create a router instance to hold endpoint definitions.
router = APIRouter()

#Asynchronously fetch data from the external API,process it, and store it into the SQLite database.
@router.get("/fetch_data")
async def fetch_data():
    
    return await Fetch_and_Store_data()


#Synchronously fetch a limited number of stored clinical trials from the database.
@router.get("/results")
def get_results(limit: int = 10): #limit (int): Number of records to return (default is 10).
    database = local_Session()
    results = get_trials(database, limit)
    database.close()

    print(f"Returned {len(results)} results")
    return {"results": results}  #Returns a JSON with a list of saved trials.




