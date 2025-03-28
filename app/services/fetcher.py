"""this file will contain the asyncronyous methods and data transformation logic"""

import aiohttp
#import pandas as pd
from datetime import datetime

#updated imports now that session, models and crud have been updated.
#importing my database session and database insertion function.
from app.db.crud import save_trials
from app.db.session import local_Session

#here are some default configuration values used in my Clinical Trials API query
BASE_URL = "https://clinicaltrials.gov/api/v2/studies"
SEARCH_QUERY = "Cancer" #json Data we are interested in for data transformation
LIMIT = 5  #this is the limit of the studies i will be pulling for testing and Debugging.

#this section below will Fetch, transform and store the clinical trial data.
async def Fetch_and_Store_data():
    #this will build the full API URL with the necessary parameters
    url = f"{BASE_URL}?format=json&query.cond={SEARCH_QUERY}&markupFormat=markdown"

    #this section will make the async HTTP request to the external API
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response .status != 200:
                return{"a Wild Error has appeared!" : f"Failed to fetch data: {response.status}"}
            
            raw_data = await response.json() #this pulls the json data from the URL API


    #this next section will Parse the return JSON and extract key information
    studies = raw_data.get("studies",[])
    data = []

    for study in studies[:LIMIT]:
        try:
            info = study["protocolSection"]
            location = info.get("contactsLocationsModule", {}).get("locations", [{}])[0]

            #Below appends a Simplified structure to a list for the database Save function.
            data.append({
                "nct_id": info["identificationModule"].get("nctId", ""),
                "title": info["identificationModule"].get("briefTitle", ""),
                "status": info["statusModule"].get("overallStatus", ""),
                "start_date": info["statusModule"]["startDateStruct"].get("date", ""),
                "summary": info["descriptionModule"].get("briefSummary", ""),
                "phase": info["designModule"].get("phases", [""])[0],
                "study_type": info["designModule"].get("studyType", ""),
                "condition": info["conditionsModule"].get("conditions", [""])[0],
                "location_city": location.get("city", ""),
                "location_state": location.get("state", ""),
            })
        except KeyError:
            continue #this should skip any bad entries with bad data.
    
    #Opens the Database Session, inserts the trials, and close the connection.
    dataBase = local_Session()
    save_trials(dataBase, data)
    dataBase.close()

    return {"count" : len(data), "data": data}
    