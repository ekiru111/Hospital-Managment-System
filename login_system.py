import mysql.connector
from search_portal import main_dashboard # This connects our scripts!

def login():
    print("\n" + "="*30)
    print("🔐 HMS SYSTEM LOGIN")
    print("="*30)
    
    username = input("Username: ")
    password = input("Password: ")

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="SFU@2025!", # Use your actual password
            database="hms_db"
        )
        cursor = db.cursor()

        # Check if user exists with that password
        query = "SELECT Role FROM Users WHERE Username = %s AND Password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            print(f"\n✅ Login Successful! Welcome, {username} ({result[0]})")
            # Grant access to the dashboard
            main_dashboard()
        else:
            print("\n❌ Invalid username or password.")

    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")
    finally:
        if db.is_connected():
            cursor.close()
            db.close()

if __name__ == "__main__":
    login()