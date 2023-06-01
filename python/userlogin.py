'''
In this updated script, we have two new functions: check_user_existence() and create_user(). 
The check_user_existence() function checks if a given username exists in the user table (a dictionary). 
The create_user() function adds a new user to the user table if the username is not found.

The read_user_log() function is modified to use these functions. If the user is not found in the user table, 
it prompts the user to create an account by calling create_user(). Otherwise, it proceeds with processing 
the log entry.

Make sure to replace 'user_log.csv' with the path to your actual user log CSV file. The user_table dictionary 
can be used to store additional user information if needed.

Note: This example assumes a simple in-memory user table represented by a dictionary.
In a real application, you would typically use a database or some persistent storage to handle user accounts.

'''

import csv

def check_user_existence(username, user_table):
    return username in user_table

def create_user(username, user_table):
    user_table[username] = {}  # You can store additional user information in the dictionary if needed

def read_user_log(csv_file, user_table):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for row in reader:
            username, timestamp, action = row
            if not check_user_existence(username, user_table):
                print(f"User '{username}' does not exist. Please create an account.")
                create_user(username, user_table)
            # Process the rest of the log entry here
            print(f"Processing log entry: Username: {username}, Timestamp: {timestamp}, Action: {action}")

# Usage
csv_file_path = 'user_log.csv'
user_table = {}  # Dictionary to store user information

read_user_log(csv_file_path, user_table)


 