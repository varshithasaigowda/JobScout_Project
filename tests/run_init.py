# run_init.py
from app import app, db
from backend.models import Job
import pandas as pd

with app.app_context():
    db.create_all()
    # Load your CSV
    df = pd.read_csv('jobs_data.csv') 
    for _, row in df.iterrows():
        job = Job(
            title=row['title'],
            company=row['company'],
            location=row['location'],
            description=row['description'],
            required_skills=row['skills'],
            experience_level=row['experience']
        )
        db.session.add(job)
    db.session.commit()
    print("🧬 Database Initialized: 100 Jobs Injected.")