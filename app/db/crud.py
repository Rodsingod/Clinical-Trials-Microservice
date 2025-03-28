""" This file will handle database insert and query functions."""

from sqlalchemy.orm import Session
from app.db import models

#the purpose of this 
def save_trials(db: Session, trials: list):
    for trial in trials:
        existing = db.query(models.clinicalTrial).filter_by(nct_id=trial["nct_id"]).first()
        if not existing:
            new_trial = models.clinicalTrial(**trial)
            db.add(new_trial)
        db.commit()


def get_trials(db: Session, limit: int = 10):
    return db.query(models.clinicalTrial).limit(limit).all()
