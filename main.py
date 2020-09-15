"""
Assignment 1
Teemo Xu
CS 166 / Fall 2020

This is a simple program for three default account use to access 4 unimplemented applications.
First user need to type in the right user name and password
Then user can type in 1-6 to access different application, only with granted permission
"""

import csv

# function to check if user use one of the three default accounts
def login(filename):
    try:
        # use csv module to open any csv file
        with open(filename, 'r') as csv_file:
            # store csv file into a list of dictionaries
            data = csv.reader(csv_file)
            for row in data:
                user[row[0]] = {'password': row[1], 'access':row[2]}

            # check if user use the right combo of account
            if user[username]['password'] == password:
                print('------- welcome, {} -------'.format(username))
            else:
                # wrong combination of username and password will terminate the program
                print("Incorrect password, terminating program...")
                exit()
    except FileNotFoundError:
        # check if the csv file exists
        print("{} not found, program terminating...".format(filename))
        exit()
    except KeyError:
        # using invalid username will terminate the program
        print("{} is not a valid username".format(username))
        exit()

# function to display menu
def menu():
    print('1. Press 1 for menu area')
    print('2. Press 2 for Time Reporting area')
    print('3. Press 3 for Accounting area')
    print('4. Press 4 for IT Helpdesk area')
    print('5. Press 5 for Engineering Documents area')
    print('6. Press 6 to close the program')

# function to check if user have the access to time reporting application
def time_reporting():
    level = user[username]['access']
    if level == '1' or level == '2' or level == '3':
        print("You are in the Time Reporting application\n")
    else:
        print("You are not authorized to access this area.\n")

# function to check if user have the access to accounting application
def accounting():
    level = user[username]['access']
    if level == '1' or level == '2' or level == '3':
        print("You are in the Accounting application\n")
    else:
        print("You are not authorized to access this area.\n")

# function to check if user have the access to IT helpdesk application
def helpdesk():
    level = user[username]['access']
    if level == '1' or level == '2':
        print("You are in the IT Helpdesk application\n")
    else:
        print("You are not authorized to access this area.\n")

# function to check if user have the access to engineering document application
def document():
    level = user[username]['access']
    if level == '1':
        print("You are in the Engineering Documents application\n")
    else:
        print("You are not authorized to access this area.\n")


if __name__ == "__main__":
    user = {}
    print("------------ Login ------------")
    # take in user's input of their user name and password
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    login("user_info.csv")
    # display menu
    menu()
    menu_choice = 0
    # while loop to make sure the program run properly, exit with 6 entered
    while menu_choice != 6:
        try:
            menu_choice = int(input("What's you choice(1 for menu, 6 for exit): "))
            if menu_choice == 1:
                menu()
            elif menu_choice == 2:
                time_reporting()
            elif menu_choice == 3:
                accounting()
            elif menu_choice == 4:
                helpdesk()
            elif menu_choice == 5:
                document()
            elif menu_choice == 6:
                pass
            else:
                # avoid anything other than 1-6 entered
                print("Invalid input.")
        except ValueError:
            # avoid anything other than number entered
            print("Invalid input.")
    print("Terminating...")



