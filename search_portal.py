import mysql.connector

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
        for row in results:
            # Handle potential None values for Bill and Status
            bill_amount = row[4] if row[4] is not None else "0.00"
            status = row[5] if row[5] is not None else "Unbilled"
            
            # Now we format the cleaned variables
            print(f"{row[0]} {row[1]:<13} | {str(row[2]):<12} | Dr. {row[3]:<11} | {str(bill_amount):<10} | {status}")
    
    cursor.close()
    db.close()

def main_dashboard():
    while True:
        print("\n" + "="*30)
        print("🏥 HMS RECEPTION DASHBOARD")
        print("="*30)
        print("1. Search Patient & Billing")
        print("2. View All Appointments (Today)")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ")

        if choice == '1':
            search_patient()
        elif choice == '2':
            # This calls the SQL VIEW we created yesterday!
            print("\nFetching today's schedule...")
            # (Logic for View could go here)
            print("Feature coming soon!") 
        elif choice == '3':
            print("👋 Logging out. Have a great day!")
            break
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main_dashboard()