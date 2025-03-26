"""This file will manage any SQLAlchemy Models"""

from sqlalchemy import Column, Integer, String
from app.db.session import base

class clinicalTrial(base):
    __tablename__= "clinical_trails"
    
    #the variables below match the information i chose to extract in the Fetcher.py file.
    id = Column(Integer, primary_key=True, index=True)
    nct_id = Column(String, unique=True, index=True)
    title = Column(String)
    status = Column(String)
    start_date = Column(String)
    summary = Column(String)
    phase = Column(String)
    study_type = Column(String)
    condition = Column(String)
    location_city = Column(String)
    location_state = Column(String)