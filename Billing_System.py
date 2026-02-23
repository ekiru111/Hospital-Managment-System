import mysql.connector

def generate_bill(appt_id, pharmacy_cost):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="SFU@2025!", # Use your actual password
            database="hms_db"
        )
        cursor = db.cursor()

        # Calculate Total
        consultation = 50000.00 # Standard fee
        total = consultation + pharmacy_cost

        # Insert into Billing table
        sql = """INSERT INTO Billing (AppointmentID, PharmacyCharges, TotalAmount, PaymentStatus) 
                 VALUES (%s, %s, %s, 'Pending')"""
        val = (appt_id, pharmacy_cost, total)
        
        cursor.execute(sql, val)
        db.commit()

        print(f"✅ Bill generated for {appt_id}. Total: {total} UGX")

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
    finally:
        if db.is_connected():
            cursor.close()
            db.close()

# Test it with one of your existing Appointment IDs (e.g., 'HMS/APPT/001')
generate_bill('HMS/APPT/001', 15000.00)