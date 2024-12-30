import mysql.connector
from random import randint
import re

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="banking_system"
)
cursor = conn.cursor()

# Utility Functions
def validate_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def validate_password(password):
    return len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password)

def validate_contact(contact):
    return re.match(r"^\d{10}$", contact)

def generate_account_number():
    return str(randint(1000000000, 9999999999))

def validate_balance(balance):
    return balance >= 2000

def add_user():
    name = input("Enter Name: ")
    dob = input("Enter DOB (YYYY-MM-DD): ")
    city = input("Enter City: ")
    email = input("Enter Email: ")
    if not validate_email(email):
        print("Invalid Email")
        return
    contact = input("Enter Contact Number: ")
    if not validate_contact(contact):
        print("Invalid Contact Number")
        return
    address = input("Enter Address: ")
    password = input("Enter Password: ")
    if not validate_password(password):
        print("Invalid Password")
        return
    account_number = generate_account_number()
    balance = int(input("Enter Initial Balance: "))
    if not validate_balance(balance):
        print("Minimum balance is 2000")
        return
    cursor.execute("INSERT INTO users (name, account_number, dob, city, email, contact, address, password, balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, account_number, dob, city, email, contact, address, password, balance))
    conn.commit()
    print("User added successfully")

def show_users():
    cursor.execute("SELECT * FROM users")
    for user in cursor.fetchall():
        print(user)

def login():
    account_number = input("Enter Account Number: ")
    password = input("Enter Password: ")
    cursor.execute("SELECT * FROM users WHERE account_number=%s AND password=%s", (account_number, password))
    user = cursor.fetchone()
    if user:
        while True:
            print("1. Show Balance\n2. Show Transactions\n3. Credit Amount\n4. Debit Amount\n5. Transfer Amount\n6. Activate/Deactivate Account\n7. Change Password\n8. Update Profile\n9. Logout")
            choice = input("Enter Choice: ")
            if choice == "1":
                print(f"Balance: {user[-1]}")
            elif choice == "2":
                cursor.execute("SELECT * FROM transactions WHERE account_number=%s", (account_number,))
                for txn in cursor.fetchall():
                    print(txn)
            elif choice == "3":
                amount = int(input("Enter Amount to Credit: "))
                cursor.execute("UPDATE users SET balance=balance+%s WHERE account_number=%s", (amount, account_number))
                conn.commit()
                print("Amount Credited")
            elif choice == "4":
                amount = int(input("Enter Amount to Debit: "))
                if user[-1] >= amount:
                    cursor.execute("UPDATE users SET balance=balance-%s WHERE account_number=%s", (amount, account_number))
                    conn.commit()
                    print("Amount Debited")
                else:
                    print("Insufficient Balance")
            elif choice == "5":
                target_account = input("Enter Target Account Number: ")
                amount = int(input("Enter Amount to Transfer: "))
                if user[-1] >= amount:
                    cursor.execute("UPDATE users SET balance=balance-%s WHERE account_number=%s", (amount, account_number))
                    cursor.execute("UPDATE users SET balance=balance+%s WHERE account_number=%s", (amount, target_account))
                    conn.commit()
                    print("Amount Transferred")
                else:
                    print("Insufficient Balance")
            elif choice == "6":
                status = input("Enter Account Status (active/inactive): ")
                cursor.execute("UPDATE users SET status=%s WHERE account_number=%s", (status, account_number))
                conn.commit()
                print("Account Status Updated")
            elif choice == "7":
                new_password = input("Enter New Password: ")
                if validate_password(new_password):
                    cursor.execute("UPDATE users SET password=%s WHERE account_number=%s", (new_password, account_number))
                    conn.commit()
                    print("Password Updated")
                else:
                    print("Invalid Password")
            elif choice == "8":
                field = input("Enter Field to Update (name, dob, city, email, contact, address): ")
                new_value = input("Enter New Value: ")
                cursor.execute(f"UPDATE users SET {field}=%s WHERE account_number=%s", (new_value, account_number))
                conn.commit()
                print("Profile Updated")
            elif choice == "9":
                print("Logged Out")
                break
            else:
                print("Invalid Choice")
    else:
        print("Invalid Login")

def main():
    while True:
        print("1. Add User\n2. Show Users\n3. Login\n4. Exit")
        choice = input("Enter Choice: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            show_users()
        elif choice == "3":
            login()
        elif choice == "4":
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
    conn.close()
