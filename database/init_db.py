import pandas as pd
import os
from app import app
from backend.models import db, Job

def init_database():
    """
    Creates all database tables and populates the Job table from the CSV dataset.
    """
    # 1. Ensure the database directory exists
    if not os.path.exists('database'):
        os.makedirs('database')
        print("Created /database directory.")

    with app.app_context():
        # 2. Create the tables based on models.py
        print("Initializing tables...")
        db.create_all()
        print("Tables created successfully.")

        # 3. Check if Jobs are already loaded to avoid duplicates
        if Job.query.first() is None:
            csv_path = 'data/jobs_dataset.csv'
            
            if os.path.exists(csv_path):
                print(f"Loading jobs from {csv_path}...")
                df = pd.read_csv(csv_path)
                
                # Fill NaN values to avoid SQL errors
                df = df.fillna('Not Specified')

                for index, row in df.iterrows():
                    new_job = Job(
                        title=row.get('title', 'Unknown Title'),
                        company=row.get('company', 'Unknown Company'),
                        location=row.get('location', 'Remote'),
                        description=row.get('description', ''),
                        required_skills=row.get('required_skills', ''),
                        salary_range=str(row.get('salary_range', 'Negotiable')),
                        experience_level=row.get('experience_level', 'Entry Level')
                    )
                    db.session.add(new_job)
                
                db.session.commit()
                print(f"Successfully imported {len(df)} jobs into the database.")
            else:
                print(f"Warning: {csv_path} not found. Job table remains empty.")
        else:
            print("Database already contains job data. Skipping import.")

if __name__ == "__main__":
    init_database()