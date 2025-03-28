# Clinical-Trials-Microservice
This project serves as a way to fetch and receive data from clinical trials provided from clinicalTrials.gov

this project is made in python code. the creation of this application required two virtual enviornments to account for differences between python 3.11 and 3.13. the updated version sits at the top of the file structure while the created virtual environment created manually for 3.11 sits at the bottom. select which ever is appropriate for your interpreter. 

Here is a good description of the nature of each file:

Session.py___________
This file Tells the app how to talk to the database.
it sets up a local SQLite file, opens a connection, and gives us a way to create or retreive records using python classes instead of SQL commands.

models.py____________