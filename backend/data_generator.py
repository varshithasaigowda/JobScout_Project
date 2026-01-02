import pandas as pd
import random, os, csv

# Unified Master Pool (Used by both Jobs and Dropdown)
skills_pool = [
    "Python Programming", "Web Development (HTML, CSS, JS)", 
    "Database Management (SQL)", "Fashion Sketching", 
    "Vocal Training", "Digital Marketing", "Cooking & Culinary Skills",
    "Machine Learning", "UI/UX Design", "Project Management"
]
companies = ["Google", "Microsoft", "Tesla", "Zara", "Netflix", "Starbucks", "Jio"]
roles = ["Software Developer", "Fashion Designer", "Data Analyst", "Digital Marketer", "Chef"]

data = []
for i in range(1, 1001):
    role = random.choice(roles)
    # REQUIREMENT: Exactly 2 to 5 skills per job
    num_required = random.randint(2, 5)
    selected_skills = random.sample(skills_pool, num_required)
    skill_set = ", ".join(selected_skills)
    
    data.append({
        "title": f"{role} {i}",
        "company": random.choice(companies),
        "location": "Remote",
        "description": f"Professional role requiring: {skill_set}.",
        "required_skills": skill_set,
        "experience_level": f"{random.randint(1, 5)}+ Years"
    })

df = pd.DataFrame(data)
if not os.path.exists('data'): os.makedirs('data')
df.to_csv('data/jobs_dataset.csv', index=False, quoting=csv.QUOTE_ALL, encoding='utf-8-sig')
print(f"✅ Generated 1000 jobs with 2-5 skills each.")