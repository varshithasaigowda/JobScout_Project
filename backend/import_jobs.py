import pandas as pd
from backend.models import create_job


def import_jobs_from_csv(csv_path):
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        create_job(
            title=row["title"],
            company=row["company"],
            location=row.get("location", ""),
            skills_required=row.get("skills_required", ""),
            salary=row.get("salary", 0),
            description=row.get("description", "")
        )
