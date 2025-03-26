"""this file will contain the asyncronyous methods and data transformation logic"""

import aiohttp
#import pandas as pd
from datetime import datetime


#here are some default values used in my Clinical Trials API test
BASE_URL = "https://clinicaltrials.gov/api/v2/studies"
SEARCH_QUERY = "Brain Tumor" #json Data we are interested in for data transformation
LIMIT = 5

#this section below i will using to list my Asyncronous functions
async def Fetch_and_Store_data():
    #this will build the URL with the necessary parameters
    url = f"{BASE_URL}?format=json&query.cond={SEARCH_QUERY}&markupFormat=markdown"


    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response .status != 200:
                return{"a Wild Error has appeared!" : f"Failed to fetch data: {response.status}"}
            
            raw_data = await response.json() #this pulls the json data from the URL API


    #this next section will serve to extract and normalize the study fields
    studies = raw_data.get("studies",[])
    data = []

    for study in studies[:LIMIT]:
        try:
            info = study["protocolSection"]
            location = info["contactsLocationModule"],["locations"][0]


            data.append({
                "nct_id": info["identificationModule"].get("nctId", ""),
                "title": info["identificationModule"].get("briefTitle", ""),
                "status": info["statusModule"].get("overallStatus", ""),
                "start_date": info["statusModule"]["startDateStruct"].get("date", ""),
                "summary": info["descriptionModule"].get("briefSummary", ""),
                "phase": info["designModule"].get("phases", [""])[0],
                "study_type": info["designModule"].get("studyType", ""),
                "condition": info["conditionsModule"].get("conditions", [""])[0],
                "location_city": info["contactsLocationsModule"]["locations"][0].get("city", ""),
                "location_state": info["contactsLocationsModule"]["locations"][0].get("state", ""),
            })
        except KeyError:
            continue #this should skip any bad entries with bad data.

    return {"count" : len(data), "data": data}
    