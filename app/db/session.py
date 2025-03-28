""" this file will Manage the Database engine and session setup"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#this line below is the path to my local SQL lite database file
DATABASE_URL = "sqlite:///./clinical_trials.db"


#next step is to create a route to the database
#for this i am using the "Check same thread" function which allows multiple threads to be used with SQL lite
database_engine = create_engine(DATABASE_URL, connect_args= {"check_same_thread": False}) #this line prevents sql crashes due to threading issues.


local_Session = sessionmaker(bind = database_engine,
                              autoflush = False,   #this prevents auto updates
                              autocommit = False   #this prevents auto commits so all commits are manual.
                                )                  #This 

#this line below is the base class that all SQLAlchemy models will inherit from
base = declarative_base()
