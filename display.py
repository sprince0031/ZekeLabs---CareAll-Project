import time
import os

buildVersion = 'v0.2-Alpha'

def graphic():
    os.system('clear')
    print("\n  .oooooo.                                      .o.       oooo  oooo")
    time.sleep(0.075)
    print(" d8P'  `Y8b                                    .888.      `888  `888")
    time.sleep(0.075)
    print('888           .oooo.   oooo d8b  .ooooo.      .8"888.      888   888')
    time.sleep(0.075)
    print('888          `P  )88b  `888""8P d88'+"' `88b    .8' `888.     888   888")
    time.sleep(0.075)
    print('888           .oP"888   888     888ooo888   .88ooo8888.    888   888')
    time.sleep(0.075)
    print("`88b    ooo  d8(  888   888     888    .o  .8'     `888.   888   888")
    time.sleep(0.075)
    print(" `Y8bood8P'  `Y888"+'""8o d888b    `Y8bod8P'+"' o88o     o8888o o888o o888o")
    time.sleep(0.25)

def pageHeader(username, loggedin):
    os.system('clear')
    print("CareAll {}\n____________________\n".format(buildVersion))
    if loggedin == 1:
        print("Welcome {}!\n{}".format(username, '_'*(len(username)+9)))