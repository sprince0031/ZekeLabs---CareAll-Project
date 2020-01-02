import display as dp

class careSeeker:
    def __init__(self, id, name, contactNo, age, location, reviewsGiven):
        self.id = id
        self.name = name
        self.contactNo = contactNo
        self.age = age
        self.location = location
        self.reviewsGiven = reviewsGiven

def userProfileCompletion(userId, newUser):
    dp.pageHeader(newUser, 1)
    print("Please enter your details in order to complete your profile. This is necessary in order for you to enjoy all services of the CareAll platform.\n")
    # TODO: a lot of same parameters as for caregiver. Care seekers have ratings and reviews too. So work this out.