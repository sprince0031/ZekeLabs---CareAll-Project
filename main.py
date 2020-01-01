import sqlite3 as sql
import hashlib
import os
import time
import stdiomask

class careGiver:
    def __init__(self, id, name, contactNo, age, currentlyTakingCareOf, location, rating, reviews):
        self.id = id
        self.name = name
        self.contactNo = contactNo
        self.age = age
        self.currentlyTakingCareOf = currentlyTakingCareOf
        self.location = location
        self.rating = rating
        self.reviews = reviews

class careSeeker:
    def __init__(self, id, name, contactNo, age, location, reviewsGiven):
        self.id = id
        self.name = name
        self.contactNo = contactNo
        self.age = age
        self.location = location
        self.reviewsGiven = reviewsGiven

def graphic():
    os.system('clear')
    print("\n  .oooooo.                                      .o.       oooo  oooo")
    print(" d8P'  `Y8b                                    .888.      `888  `888")
    print('888           .oooo.   oooo d8b  .ooooo.      .8"888.      888   888')
    print('888          `P  )88b  `888""8P d88'+"' `88b    .8' `888.     888   888")
    print('888           .oP"888   888     888ooo888   .88ooo8888.    888   888')
    print("`88b    ooo  d8(  888   888     888    .o  .8'     `888.   888   888")
    print(" `Y8bood8P'  `Y888"+'""8o d888b    `Y8bod8P'+"' o88o     o8888o o888o o888o")
    print("\nCoded with <3 by Siddharth Prince.\nEmail: siddharthprince31@gmail.com\nGithub: https://github.com/sprince0031\nLinkedIn: https://linkedin.com/in/sprince0031\nCareAll project link: https://github.com/sprince0031/ZekeLabs-CareAll-Project")

def login():
    attempts = 0
    while True:
        os.system('clear')
        print("LOGIN:\n______")
        print("Enter BACK to go back")
        username = input("Username: ").lower()
        if username == 'back':
            return
        # userType = input("1. Care giver/ 2. Care seeker? (Enter 1 or 2): ")
        cur.execute("SELECT * FROM auth WHERE username = ?", (username, ))
        row = cur.fetchone()
        if row is None:
            print("This user does not exist. Please register first or try again.")
            time.sleep(2)
            continue
        else:
            while attempts < 3:
                password = stdiomask.getpass()
                pwd = hashlib.sha256(password.encode('utf-8')).hexdigest()
                if pwd == row[2]:
                    newUser = row[4]
                    cur.execute("UPDATE auth SET loggedin = 1 WHERE username = ?", (username, ))
                    con.commit()
                    cur.execute("SELECT username, usertype, lastlogin FROM auth WHERE username = ?", (username, ))
                    row = cur.fetchone()
                    print("Last login:", row[2])
                    time.sleep(2)
                    # print(newUser)
                    return row
                else:
                    attempts += 1
                    print("Wrong password! You have {} attempt(s) remaining".format(3 - attempts))
            print("Login failed! Going back to home screen...")
            time.sleep(2)
            return
            

def register():
    
    while True:
        os.system('clear')
        print("REGISTER:\n_________")
        print("Enter BACK to go back")
        username = input("Username: ").lower()
        if username == 'back':
            return
        cur.execute("SELECT username FROM auth WHERE username = ?", (username, ))
        row = cur.fetchone()
        if row is None:
            while True:
                # print("Enter BACK to go back")
                password = stdiomask.getpass()
                if password.lower() == 'back':
                    break
                if len(password) < 8:
                    print("Password length too short. Please try again.")
                    continue
                cpass = stdiomask.getpass(prompt='Confirm password: ')
                if password != cpass:
                    print("Passwords don't match. Please try again!")
                else:
                    print("Passwords match!")
                    break
            if password.lower() == 'back':
               continue
            pwd = hashlib.sha256(password.encode('utf-8')).hexdigest()
            while True:
                userType = int(input("Are you a 1. Care giver/ 2. Care seeker? (Enter 1 or 2): "))
                if userType == 1:
                    tableName = "careGiver"
                    break
                elif userType == 2:
                    tableName = "careSeeker"
                    break
                else:
                    print("Please enter a valid option and try again.")
            cur.execute("INSERT INTO auth (username, password, usertype, loggedin) VALUES (?, ?, ?, -1)", (username, pwd, userType))
            con.commit()
            print("User successfully created! Please login to continue.")
            return login()
            
        else:
            print("Username already exists! Please try again.")

def logout(username):
    cur.execute("UPDATE auth SET loggedin = 0 WHERE username = ?", (username, ))
    con.commit()
    cur.execute("SELECT lastlogin FROM auth WHERE username = ?", (username, ))
    row = cur.fetchone()
    print("Logged out at", row[0])
    time.sleep(2)
    return

# if "__name__" == "__main__":
graphic()
print("Welcome to the CareAll Application!\n")
time.sleep(2.5)
con = sql.connect("careall.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS auth 
(id INT AUTO_INCREMENT PRIMARY KEY,
username NVARCHAR(150) NOT NULL,
password NVARCHAR(256) NOT NULL,
usertype INT(1) NOT NULL,
loggedin INT(1) CHECK (loggedin IN (1, 0, -1)),
lastlogin TIMESTAMP DEFAULT CURRENT_TIMESTAMP);''')
while True:
    os.system('clear')
    print("CareAll (v0.1-Alpha)\n____________________\n")
    print("Enter EXIT to exit the program.")
    loginChoice = input("1. Login/ 2. New User? (Enter 1 or 2): ")
    if loginChoice.lower() == "exit":
        graphic()
        con.close()
        print("Exiting program...")
        exit()
    loginChoice = int(loginChoice)
    if loginChoice == 1:
        userData = login()
    elif loginChoice == 2:
        userData = register()
    else:
        print("Please enter a valid option and try again.")
    if userData == None:
        continue
    else:
        os.system('clear')
        while True:
            print("CareAll (v0.1-Alpha)\n____________________\n\n")
            print("Welcome {}!\n{}".format(userData[0], '_'*(len(userData[0])+9)))
            print("What do you want to do?\n0. Logout")
            action = int(input("Enter choice: "))
            if action == 0:
                logout(userData[0])
                break
        


