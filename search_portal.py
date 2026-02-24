import mysql.connector
import csv

# This must be at the top level (no spaces at the start of the line)
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SFU@2025!", # Use your actual password
        database="hms_db"
    )

def search_patient():
    db = connect_db()
    cursor = db.cursor()
    search_name = input("\n🔍 Enter Patient Last Name to search: ")
    
    query = """
    SELECT p.FirstName, p.LastName, a.AppointmentDate, d.LastName, b.TotalAmount, b.PaymentStatus
    FROM Patients p
    JOIN Appointments a ON p.PatientID = a.PatientID
    JOIN Doctors d ON a.DoctorID = d.DoctorID
    LEFT JOIN Billing b ON a.AppointmentID = b.AppointmentID
    WHERE p.LastName LIKE %s
    """
    cursor.execute(query, (f"%{search_name}%",))
    results = cursor.fetchall()

    if results:
        print(f"\n{'NAME':<20} | {'DATE':<12} | {'DOCTOR':<15} | {'BILL':<10} | {'STATUS'}")
        print("-" * 80)

        # STEP 1: Just print the names (Loop starts here)
        for row in results:
            bill_amount = row[4] if row[4] is not None else "0.00"
            status = row[5] if row[5] is not None else "Unbilled"
            print(f"{row[0]} {row[1]:<13} | {str(row[2]):<12} | Dr. {row[3]:<11} | {str(bill_amount):<10} | {status}")
        # (Loop ends here)

        # STEP 2: Now ask once (Notice the indentation moves back to the left!)
        export = input("\n💾 Would you like to export these results to a CSV file? (y/n): ").lower()
        if export == 'y':
            filename = f"search_export_{search_name}.csv"
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['First Name', 'Last Name', 'Date', 'Doctor', 'Amount', 'Status'])
                writer.writerows(results)
            print(f"✅ Success! Report saved as {filename}")
            
    else:
        print("❌ No records found.")
    
    cursor.close()
    db.close()


def view_today_schedule():
    db = connect_db()
    cursor = db.cursor()
    
    # We are calling the VIEW we created in MySQL yesterday!
    query = "SELECT * FROM daily_hospital_schedule"
    
    cursor.execute(query)
    results = cursor.fetchall()

    print("\n--- 📅 TODAY'S APPOINTMENT SCHEDULE ---")
    if results:
        print(f"{'ID':<12} | {'PATIENT':<20} | {'DOCTOR':<15} | {'STATUS'}")
        print("-" * 65)
        for row in results:
            # row[0]=ID, row[1]=Patient, row[2]=Doctor, row[5]=Status
            print(f"{row[0]:<12} | {row[1]:<20} | {row[2]:<15} | {row[5]}")
    else:
        print("📭 No appointments scheduled for today.")
    
    cursor.close()
    db.close()

def main_dashboard():
    while True:
        print("\n" + "="*30)
        print("🏥 HMS RECEPTION DASHBOARD")
        print("="*30)
        print("1. Search Patient & Billing")
        print("2. View All Appointments (Today's View)")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ")

        if choice == '1':
            search_patient()
        elif choice == '2':
            view_today_schedule() # Now this works!
        elif choice == '3':
            print("👋 Logging out. Have a great day!")
            break
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main_dashboard()
