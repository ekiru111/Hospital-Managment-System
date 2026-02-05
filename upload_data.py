import mysql.connector
import csv

# 1. Connect to MySQL
db_config = {
    "host": "localhost",
    "user": "root",        # Replace with your MySQL username
    "password": "SFU@2025!", # Replace with your MySQL password
    "database": "hms_db"
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    def upload_csv(filename, table_name):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)  # Skip the header row
            
            # Prepare the INSERT statement
            cols = ", ".join(header)
            placeholders = ", ".join(["%s"] * len(header))
            sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
            
            for row in reader:
                cursor.execute(sql, row)
        
        conn.commit()
        print(f"Successfully uploaded {filename} to {table_name}!")

    # 2. Upload in order (Patients & Doctors first, then Appointments)
    upload_csv('patients_data.csv', 'Patients')
    upload_csv('doctors_data.csv', 'Doctors')
    upload_csv('appointments_data.csv', 'Appointments')

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()