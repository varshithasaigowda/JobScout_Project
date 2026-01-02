from backend import models

# Example: mark application ID 1 as accepted
conn = models.get_connection()
cursor = conn.cursor()
cursor.execute("UPDATE applications SET status = 'accepted' WHERE id = 1")
conn.commit()
conn.close()

print("Application status updated successfully!")
