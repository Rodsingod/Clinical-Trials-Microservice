from app.db.session import database_engine, base
from app.db import models

# Create the tables defined in models.py
base.metadata.create_all(bind=database_engine)

print("Database and tables created successfully.")