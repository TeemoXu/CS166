# CS166
## assignment 1
Write a Python program: Create a login and menu to a company intranet system that requires users (employees) to enter a 
username and password in order to view a menu of options (such as Time Reporting, Accounting, IT Helpdesk, Engineering 
Documents, etc.). 

Technical requirements:

1. Plaintext usernames/passwords/access level stored in a csv (or text) file
2. Create three different access levels (roles for different users). For example, User A should have 
access to all menu items ('admin' access), while User B has limited access (no Accounting or Engineering 
Documents), etc. 
3. Once logged in the user should be able to select different menu options with a number input (for 
example, "press 1 for the Time Reporting area", "press 2 for the Accounting area", etc.).
4. When a user enters a menu area they have access to, a simple message similar to 'You have now 
accessed the accounting application' is sufficient to indicate a successful demonstration of the access 
control (no need to build out any actual accounting functionality). Likewise, if a user does not have 
the appropriate access level to view a menu area, the program should display a 'You are not authorized 
to access this area.' message and provide an option to return them to the main menu.
5. Good programming practices: Must adhere to Python PEP8 style guide (refer to style guide reference 
PDF posted in this module). Reasonable amount of error/exception handling. Must organize code into 
functions (no duplicate code!). Well-documented. Written in Python 3. No GUI, this should be a command 
menu driven program.

### how to run the program
make sure put main.py and user_info.csv in the same directory, and open command line tool, find the directory, and type 
"python main.py".
1. username: user_a, password: admin - can access to all applications
2. username: user_b, password: limited1 - can access all except the last application
3. username: user_c, password: limited2 - can access menu and time reporting

make sure username and password are typed correctly, otherwise the program will terminate, after log in,
there is no need to worry about the what to input, program will not terminate

inside the program, there should be enough instruuction to run the program