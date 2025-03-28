"""This file will test the Results Endpoint in FastAPI"""

from fastapi.testclient import TestClient #this import simulates request to the api 
from main import app



client = TestClient(app)

def test_results_endpoint():
    response = client.get("/results")    #this Simulates sending a GET request to the /results endpoint, just like a user or Postman would.
    assert response.status_code == 200   #Confirms that the API responded with HTTP status 200 (OK).
    assert "results" in response.json()  #this line will Confirms that the returned JSON contains a key called "results".
