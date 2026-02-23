import mysql.connector

def search_patient():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="SFU@2025!", # Use your actual password
            database="hms_db"
        )
        cursor = db.cursor()

        # Get user input
        search_name = input("🔍 Enter Patient Last Name: ")

        # Complex SQL Join to fetch Patient, Appointment, and Billing info
        query = """
        SELECT p.FirstName, p.LastName, a.AppointmentDate, d.LastName, b.TotalAmount, b.PaymentStatus
        FROM Patients p
        JOIN Appointments a ON p.PatientID = a.PatientID
        JOIN Doctors d ON a.DoctorID = d.DoctorID
        LEFT JOIN Billing b ON a.AppointmentID = b.AppointmentID
        WHERE p.LastName LIKE %s
        """
        
        # Use % with the search name for a "partial match" (e.g., 'Mu' finds 'Mugisha')
        cursor.execute(query, (f"%{search_name}%",))
        results = cursor.fetchall()

        print("\n--- 📋 SEARCH RESULTS ---")
        if results:
            for row in results:
                print(f"Patient: {row[0]} {row[1]}")
                print(f"Date: {row[2]} | Doctor: Dr. {row[3]}")
                print(f"Bill: {row[4]} UGX | Status: {row[5]}")
                print("-" * 25)
        else:
            print("❌ No patient found with that name.")

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
    finally:
        if db.is_connected():
            cursor.close()
            db.close()

if __name__ == "__main__":
    search_patient()