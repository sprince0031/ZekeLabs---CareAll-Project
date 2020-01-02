import sqlite3 as sql
import hashlib
import os
import time
import stdiomask
import caregiver as cg
import careseeker as cs
import display as dp

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
                    cur.execute("SELECT id, username, usertype, loggedin, lastlogin FROM auth WHERE username = ?", (username, ))
                    row = cur.fetchone()
                    print("Last login:", row[4])
                    time.sleep(2)
                    # print(newUser)
                    return row[0], row[1], row[2], row[3], row[4], newUser
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
                # if userType == 1:
                #     tableName = "careGiver"
                #     break
                # elif userType == 2:
                #     tableName = "careSeeker"
                #     break
                if userType in [1, 2]:
                    break
                else:
                    print("Please enter a valid option and try again.")
            cur.execute("INSERT INTO auth (username, password, usertype, loggedin) VALUES (?, ?, ?, -1)", (username, pwd, userType))
            con.commit()
            print("User successfully registered! Please login to continue.")
            time.sleep(2)
            return login()
            
        else:
            print("Username already exists! Please try again.")
            time.sleep(2)

def logout(username):
    cur.execute("UPDATE auth SET loggedin = 0 WHERE username = ?", (username, ))
    con.commit()
    cur.execute("SELECT lastlogin FROM auth WHERE username = ?", (username, ))
    row = cur.fetchone()
    print("Logged out at", row[0])
    time.sleep(2)
    return 0

if __name__ == '__main__':
    dp.graphic()
    print("\nWelcome to the CareAll Application!\n")
    time.sleep(2)
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
        dp.pageHeader("", 0)
        print("Enter EXIT to exit the program.")
        loggedIn = 0
        loginChoice = input("1. Login/ 2. New User? (Enter 1 or 2): ")
        if loginChoice.lower() == "exit":
            dp.graphic()
            con.close()
            print("\nCoded with <3 by Siddharth Prince.\nEmail: siddharthprince31@gmail.com\nGithub: https://github.com/sprince0031\nLinkedIn: https://linkedin.com/in/sprince0031\nCareAll project link: https://github.com/sprince0031/ZekeLabs-CareAll-Project\n")
            print("Exiting program...")
            exit()
        loginChoice = int(loginChoice)
        if loginChoice == 1:
            userId, userName, userType, loggedIn, lastLogin, newUser = login()
        elif loginChoice == 2:
            userId, userName, userType, loggedIn, lastLogin, newUser = register()
        else:
            print("Please enter a valid option and try again.")
        if userName == None:
            continue
        else:
            os.system('clear')
            # if newUser == -1:
            if userType == 1:
                cg.main(userId, userName, loggedIn, newUser)
                loggedIn = logout(userName)
            if userType == 2:
                cs.main(userId, userName, loggedIn, newUser)
                loggedIn = logout(userName)
            
        


