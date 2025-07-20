# PDBC_Connection

# mysql.connector is a python driver which is used to interact with Mysql databases
# This module must be installed via pip install mysql-connector-python

# There are 3 steps to establish a JDBC connection
# step-1: Import and install mysql-connector
# step-2: Establish connection using connect() method available in mysql.connector driver
# step-3: Check weather the connection is sucessfully established or not

# step-1:Import and install mysql-connector

import mysql.connector

def dbConnect():
    # connect() method creates a connection object by calling the connect() method available in mysql.connector driver.
    # It takes 4 parameters:
        # ->hostname
        # ->databasename
        # ->username
        # ->password

    # step-2: Establish connection using connect() method using mysql.connector
    connection = mysql.connector.connect(
        host='localhost',
        database='PDBC',
        user='root',
        password='Your database password'
    )
    
    # if all the given inputs are matched ,it returns a live connection object.

    # step-3: Check weather the connection is sucessfully established or not.
    # is_connected() is a method that returns True if the connection is open and valid.
    if connection.is_connected():
        print("Connection Established")
        return connection
    return None
dbConnect()

# Wrapping your connect() logic in a try-except block helps handle connection errors gracefully 
# rather than letting the program crash when something goes wrong 
# (like wrong credentials or server not running).

# The following code will be Wrapped in a try-except block

# import mysql.connector
# from mysql.connector import Error
# def connect():
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             database='PDBC',
#             user='root',
#             password='Your database password'
#         )
#         if connection.is_connected():
#             print("Connection Established")
#             return connection
#     except Error as e:
#         print(f"Connection Failed: {e}")
#     return None
# connect()
