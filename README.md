# Banking Application

A simple banking system with various user functionalities, including user creation, login, balance management, and transaction features. This project is designed to demonstrate basic banking operations and ensure user security through validations.

---
## Submission Details

- **Submitted To**: Training and Placement (TnP) Department
- **Assessment Type**: College Submission
- **Submitted By**: Nikhil Raikwar
- **Enrollment Number**: 0103IS221130
- **Branch**: CSE-IOT & CS

---

## Features

### 1. **Add User**
- Users can be added to the system with the following fields:
  - **Name**
  - **Account Number**: A randomly generated unique 10-digit number.
  - **Date of Birth (DOB)**: User's date of birth in the format `YYYY-MM-DD`.
  - **City**: User's city of residence.
  - **Password**: Properly validated password (minimum 8 characters, with at least one uppercase letter and one digit).
  - **Initial Balance**: Minimum balance of 2000.
  - **Contact Number**: User's 10-digit contact number.
  - **Email ID**: User's email address.
  - **Address**: User's physical address.

All fields undergo validation rules to ensure that user input is correct.

### 2. **Show User**
- Display information about users in a readable format.

### 3. **Login**
- Users can log in by providing their account number and password.
- Once logged in, users can perform various actions:
  - **Show Balance**: Display the current account balance.
  - **Show Transactions**: View all transactions related to the user's account.
  - **Credit Amount**: Deposit funds into the user's account.
  - **Debit Amount**: Withdraw funds from the user's account (if sufficient balance exists).
  - **Transfer Amount**: Transfer funds to another user's account.
  - **Activate/Deactivate Account**: Change the status of the user's account to active or inactive.
  - **Change Password**: Update the user's password.
  - **Update Profile**: Modify personal details such as name, DOB, email, etc.
  - **Logout**: End the session and log out of the system.

### 4. **Exit**
- Close the application.

---

## Database Structure

### Database Name: `banking_system`

### Tables:

1. **users**
   - `name`: User's name.
   - `account_number`: Unique 10-digit account number.
   - `dob`: User's date of birth.
   - `city`: User's city of residence.
   - `password`: User's password.
   - `balance`: Current balance in the user's account.
   - `contact`: User's contact number.
   - `email`: User's email address.
   - `address`: User's address.
   - `status`: Account status (`active` or `inactive`).

2. **login**
   - `account_number`: Unique 10-digit account number (used for login).
   - `password`: User's password.

3. **transactions**
   - `account_number`: Account number related to the transaction.
   - `transaction_type`: Type of transaction (`credit`, `debit`, `transfer`).
   - `amount`: Amount involved in the transaction.
   - `transaction_date`: Date and time of the transaction.

---

## Requirements

- Python 3.x
- MySQL Server
- `mysql-connector` Python library
- Regular expression (for email, password, contact validation)

---

## Setup Instructions

1. **Clone or Download the Project**:
   - Clone the repository or download the `banking_system.py` file.

2. **Install Dependencies**:
   - Install the required Python libraries by running:
     ```bash
     pip install mysql-connector
     ```

3. **Setup Database**:
   - Create a database called `banking_system` in your MySQL server:
     ```sql
     CREATE DATABASE banking_system;
     ```
   - Use the provided table structure to create the necessary tables:
     ```sql
     CREATE TABLE users (
         name VARCHAR(100),
         account_number VARCHAR(10) PRIMARY KEY,
         dob DATE,
         city VARCHAR(50),
         password VARCHAR(50),
         balance DECIMAL(10, 2),
         contact VARCHAR(10),
         email VARCHAR(100),
         address TEXT,
         status VARCHAR(10) DEFAULT 'active'
     );

     CREATE TABLE login (
         account_number VARCHAR(10) PRIMARY KEY,
         password VARCHAR(50)
     );

     CREATE TABLE transactions (
         account_number VARCHAR(10),
         transaction_type VARCHAR(10),
         amount DECIMAL(10, 2),
         transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );
     ```

4. **Configure Database Credentials**:
   - In the Python code, replace the `host`, `user`, `password`, and `database` parameters with your own MySQL server credentials:
     ```python
     conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="your_password",
         database="banking_system"
     )
     ```

5. **Run the Application**:
   - Run the Python application:
     ```bash
     python banking_system.py
     ```

---

## Validation Rules

- **Email**: Must follow the format `username@domain.com`.
- **Password**: Minimum 8 characters, at least one uppercase letter, one lowercase letter, and one digit.
- **Contact Number**: Must be a valid 10-digit number.
- **Initial Balance**: Minimum balance should be 2000.
- **Account Number**: Automatically generated as a unique 10-digit number.
- **Name**: Only alphabetic characters and spaces.

---

## Contributing

1. Fork this repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request with a detailed description of the changes made.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgements

- Inspired by real-world banking systems.
- Developed to demonstrate basic banking features with Python and MySQL.

---


