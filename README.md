# Clinical-Trials-Microservice
This project serves as a way to fetch and receive data from clinical trials provided from clinicalTrials.gov
It transforms and stores selected fields into a SQLite database
it also provides 2 API endpoints to fetch new data and view results

# Features Included
this application utilizes Async data fetching using aiohttp
Data transformation and storing are handled using Naitive Python and SQLAlchemy with SQLite
I used FastAPI as my RESTAPI
I also included a Pytest file for basic testing after the database has been created.

# Requirements.
this project is made in python code. the creation of this application required two virtual enviornments to account for differences between python 3.11 and 3.13. the updated version sits at the top of the file structure while the created virtual environment created manually for 3.11 sits at the bottom. select which ever is appropriate for your interpreter. 

For Conveinience make sure you have GIT

# Installation
STEP 1. make sure you Clone the repository in the drive your python files are located to prevent pathENV issues.
cd <your-workspace-folder>
git clone https://github.com/Rodsingod/Clinical-Trials-Microservice.git
cd Clinical-Trials-Microservice

STEP 2. Make sure you create a Virtual environment
python -m venv venv
#You can activate the virtual environment on Windows
venv\Scripts\activate

STEP3. Finally you can Install the dependencies
pip install -r requirements.txt

# How to Run
STEP 1. Initialize the database tables
Run: python app/db/create_db.py

STEP 2. Start the FastAPI server
Run Main.py
in your Browser access the FastAPI UI by going to the URL: [127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
