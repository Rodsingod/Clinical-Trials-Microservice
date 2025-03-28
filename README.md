after following the Install instructions you will be able to run the program and pull clinical trial data.
1. Clone the Repo
git clone https://github.com/Rodsingod/Clinical-Trials-Microservice.git
cd Clinical-Trials-Microservice

2. Create a Virtual Environment then Activate.
python -m venv venv

venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Initialize the Database
python app/db/create_db.py

5. Run the FastAPI App
Execute Run in Main.py 


In FastAPI you will be able to use both the Get/ Fetch_Data async to pull clinical trial data from the API endpoint,
or Get/ results to view the data that has been Stored in the database to a limit 10.