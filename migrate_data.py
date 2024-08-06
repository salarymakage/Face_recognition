# migrate_data.py

import sqlite3
from detection.models import Student

# Connect to the external SQLite database
conn = sqlite3.connect("sqlite.db")
cursor = conn.execute("SELECT id, FirstName, LastName, Gender, MedicalCondition, Address, EmergencyContact FROM STUDENTS")

# Iterate through the rows in the external database
for row in cursor:
    # Create a new Student object for each row
    student = Student(
        id=row[0],
        FirstName=row[1],
        LastName=row[2],
        Gender=row[3],
        MedicalCondition=row[4],
        Address=row[5],
        EmergencyContact=row[6]
    )
    # Save the Student object to the Django database
    student.save()

# Close the connection to the external database
conn.close()
