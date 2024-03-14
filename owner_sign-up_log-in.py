import mysql.connector
from getpass import getpass
import re
# from subprocess import call


def connect_to_database():
    # Replace these values with your MySQL server details
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='ayushkumar@2004',
        database='registration'
    )
    
    
    
def check_email():
    try:
        while True:
            email = input("Email id: ")
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if(re.fullmatch(regex, email)):
                    print("Valid Email")
                    break
            else:
                print("Invalid Email")
                continue
        return str(email)
    
    except Exception as er:
        print(er)
        
        
    


def check_pwd():
    while True:
        password = input("Enter your password: ")
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
            confirm_password = input("Confirm your password: ")
            if password == confirm_password:
                print("Password confirmed")
                break
            else:
                print("Passwords do not match. Please try again.")

        else:
            print("Invalid password. It must be at least 8 characters long and can only contain letters, digits, and the following special characters: @#$%^&+=")
            continue
    return password
        
 
 
        

def check_phn():
    while True:
        phone_num = input("phone_num: ")
        regex = r'^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[6789]\d{9}|(\d[ -]?){10}\d$'
        if(re.fullmatch(regex, phone_num)):
            print("valid phone_num")
            break
        else:
            print("incorrect phone_num")
            continue
    return int(phone_num)
        
        
 
 
 
        

# def check_vehicle():
#     while True:
#         vehicle_num = input("vehicle-num: ")
#         regex = r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'
#         if(re.fullmatch(regex, vehicle_num)):
#             print("valid vehicle_num")
#             break
#         else:
#             print("incorrect vehicle_num and must be in UPPERCASE")
#             continue
#     return str(vehicle_num)
        
    
    
    

def signup():
    try:
        name = input("Name: ")
        e = check_email()
        w = check_pwd()
        p=check_phn()
        address = input("address: ")
        parking_lot_address = input("Where is your parking lot: ")
        adhar_number = input("Enter your Adhar number: ")
        area_of_plot = input("Enter Area of your plot: ")
        two_vehicle = input("No. of two vechile can be park: ")
        four_vehicle = input("No. of four vechile can be park: ")
        max_vehicle = input("Enter Max vehicle can be parked: ")
        
        # v = check_vehicle()

        connection = connect_to_database()
        # create_user_table(connection)

        cursor = connection.cursor()
        
        # Check if the email or phone_num already exists in the database
        cursor.execute("SELECT * FROM registration WHERE email = %s OR phone_num = %s OR adhar_number = %s", (e, p, adhar_number))
        existing_user = cursor.fetchone()

        if existing_user:
            print("User with the same email or phone_num or adhar_number already exists. Please use a different email or phone_num or adhar_number.")
        else:
            # Insert the new user if not already present
            query = "INSERT INTO registration (name, email, phone_num, password, address, parking_lot_address, area_of_plot, max_vehicle, two_vehicle, four_vehicle) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            data = (name, e, p, w, address, parking_lot_address, area_of_plot, max_vehicle, two_vehicle, four_vehicle)
            
            cursor.execute(query,data)
            connection.commit()
            cursor.close()
            connection.close()
            print("You're Successfully sign-up now you can log-in")
            login()
    except Exception as q:
        print(q)








def login():
    try:
        email = input("Enter your email: ")
        password = getpass("Enter your password: ")

        connection = connect_to_database()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM registration WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()

        if user:
            print("Login successful!")
            
        else:
            print("Invalid email or password.")
            login()

        cursor.close()
        connection.close()
    except Exception as o:
        print(o)
    

if __name__ == "__main__":
    choice = input("Do you want to (1) Signup or (2) Login? ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    else:
        print("Invalid choice.")
    
