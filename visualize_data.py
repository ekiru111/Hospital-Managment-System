import mysql.connector
import matplotlib.pyplot as plt

# 1. Connect to your database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SFU@2025!", # Replace with your actual password
    database="hms_db"
)
cursor = db.cursor()

# 2. Query to get appointment counts per department
query = """
SELECT d.Department, COUNT(a.AppointmentID) 
FROM Doctors d
LEFT JOIN Appointments a ON d.DoctorID = a.DoctorID
GROUP BY d.Department;
"""
cursor.execute(query)
results = cursor.fetchall()

# 3. Prepare data for the chart
departments = [row[0] for row in results]
counts = [row[1] for row in results]

# 4. Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(departments, counts, color='skyblue', edgecolor='navy')
plt.xlabel('Hospital Department', fontweight='bold')
plt.ylabel('Number of Appointments', fontweight='bold')
plt.title('Appointment Distribution by Department', fontsize=14)
plt.xticks(rotation=45)

# 5. Save the chart as an image
plt.tight_layout()
plt.savefig('appointment_chart.png')
print("Success! 'appointment_chart.png' has been created.")

cursor.close()
db.close()