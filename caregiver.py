import display as dp
import sqlite3 as sql

class careGiver:
    def __init__(self, id, name, contactNo, age, location, currentlyTakingCareOf, rating, reviews):
        self.id = id
        self.name = name
        self.contactNo = contactNo
        self.age = age
        self.location = location
        self.currentlyTakingCareOf = currentlyTakingCareOf
        self.rating = rating
        self.reviews = reviews

def userProfileCompletion(userId):
    
    print("Please enter your details in order to complete your profile. This is necessary in order for you to enjoy all services of the CareAll platform.\n")
    name = input("Full name: ")
    while True:
        try:
            contactNo  = int(input("Contact number: "))
            if len(str(contactNo)) == 10 or (len(str(contactNo)) == 11 and str(contactNo)[0] == '0'):
                break
            else:
                print("Please enter a valid phone number.")
        except:
            print("Please enter only numerical values.")
    while True:
        try:
            age = int(input("Age: "))
            break
        except:
            print("Please enter only numerical values.")
    location = input("Address:\n")
    cgUser = careGiver(userId, name, contactNo, age, location, [], 0.0, [])
    return cgUser

def main(userId, userName, loggedIn, newUser):
    dp.pageHeader(userName, loggedIn)
    con = sql.connect("careall.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS caregiver 
    (id INT PRIMARY KEY,
    name NVARCHAR(150) NOT NULL,
    age INT(3) NOT NULL,
    contact INT(11) NOT NULL,
    location TEXT NOT NULL,
    responsibleFor TEXT,
    rating FLOAT,
    reviews TEXT);''')
    # TODO: create the db entry for new user in prev method itself and let the object be created uniformly here instead.
    if newUser == -1:
        user = userProfileCompletion(userId)
    while True:
        dp.pageHeader(userName, loggedIn)
        print("What do you want to do?\n1. Display profile\n2. Edit Profile\n0. Logout")
        action = int(input("Enter choice: "))
        if action == 0:
            return
        elif action == 1:
            print("Username: {}\nName: {}\nAge: {}\nContact: {}\nAddress: {}\n".format(userName, user.name, user.age, user.contactNo, user.location))
    