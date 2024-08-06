import os
import sqlite3
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'face_detection_project.settings')
django.setup()

from detection.models import Student

def sync_data():
    try:
        conn = sqlite3.connect("sqlite.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, FirstName, LastName, Gender, MedicalCondition, Address, EmergencyContact FROM STUDENTS")
        sqlite_students = cursor.fetchall()
        conn.close()

        for student in sqlite_students:
            _, created = Student.objects.get_or_create(
                id=student[0],
                defaults={
                    'FirstName': student[1],
                    'LastName': student[2],
                    'Gender': student[3],
                    'MedicalCondition': student[4],
                    'Address': student[5],
                    'EmergencyContact': student[6],
                }
            )
        print("Data synchronization successful.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    sync_data()
