'''
Assignment 1
Teemo Xu
CS 166 / Fall 2020

Write a Python program: Create a login and menu to a company intranet system that requires users (employees) to enter a
username and password in order to view a menu of options (such as Time Reporting, Accounting, IT Helpdesk, Engineering
Documents, etc.).

Technical requirements:

Plaintext usernames/passwords/access level stored in a csv (or text) file Create three different access levels (roles
for different users). For example, User A should have access to all menu items ('admin' access), while User B has
limited access (no Accounting or Engineering Documents), etc.
Once logged in the user should be able to select different menu options with a number input (for example, "press 1 for
the Time Reporting area", "press 2 for the Accounting area", etc.).
When a user enters a menu area they have access to, a simple message similar to 'You have now accessed the accounting
application' is sufficient to indicate a successful demonstration of the access control (no need to build out any actual
accounting functionality). Likewise, if a user does not have the appropriate access level to view a menu area, the
program should display a 'You are not authorized to access this area.' message and provide an option to return them to
the main menu.
Good programming practices: Must adhere to Python PEP8 style guide (refer to style guide reference PDF posted in this
module). Reasonable amount of error/exception handling. Must organize code into functions (no duplicate code!).
Well-documented. Written in Python 3. No GUI, this should be a command menu driven program.
Please submit a compressed folder containing all of the files associated with your assignment, as well as instructions
for testing your program. Note: you will be adding functionality to this system in a subsequent assignment, so take your
time and plan out your design.
'''
import csv

def loginInfo(dict, filename):
    with open(filename, 'r') as csv_file:
        data = csv.reader(csv_file, delimiter = ' ')
        for row in data:
            print(', '.join(row))


def login():
    print("------------ Login ------------")
    user_name = input("username: ").strip()
    print("Password: ")

if __name__ == "__main__":
    users = {}
    loginInfo(users, "User_info.csv")
