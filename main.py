import sqlite3
import os
import lib.checkStrUtils as checkStrUtils
from lib.User import User



def clearConsole():
    os.system('clear')


def checkIfUsernameIsUniqueInDB(username):
    con = sqlite3.connect("incollege.db")
    cur = con.cursor()
    res = cur.execute(
        "SELECT user_username FROM users WHERE user_username = ? LIMIT 1",
        (username, ))
    user = res.fetchone()
    return user == None


def checkPassword(password):
    if not checkStrUtils.checkIfStrIsCorrectLength(password, 8, 12):
        print("\tPassword must be 8-12 characters in length ")
        return False

    if not checkStrUtils.checkIfStrContainsUpperChar(password):
        print("\tPassword must contain at least 1 uppercase character ")
        return False

    if not checkStrUtils.checkIfStrContainsDigit(password):
        print("\tPassword must contain at least 1 digit ")
        return False

    if not checkStrUtils.checkIfStrContainsSpecialChar(password):
        print("\tPassword must contain at least 1 special character ")
        return False

    return True


def login():
    clearConsole()
    print("\n\tLogin Screen")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    tempUser = User(None)
    user = tempUser.findOneByUsername(username)

    if (user == None or user[2] != password):
        print("\tIncorrect username or password!\n\tPlease try again.\n")
        login()
    else:
        print("\tYou have successfully logged in\n")
        clearConsole()
        loggedInUser = User(user[0])
        optionsScreen(loggedInUser)


def checkUsername(username):
    if (not checkStrUtils.checkIfStrIsCorrectLength(username, 1, 32)):
        print(
            "\tUsername must be between 1 and 32 characters!\n\tPlease try again.\n"
        )
        return False
    if (not checkIfUsernameIsUniqueInDB(username)):
        print("\tUsername must be unique!\n\tPlease try again.\n")
        return False
    return True


def signup():
    clearConsole()
    print("\tSignup Screen")
    con = sqlite3.connect("incollege.db")
    cur = con.cursor()
    res = cur.execute("SELECT COUNT() FROM users")
    userCount = res.fetchone()[0]
    print("Number of Users: " + str(userCount))

    if (userCount >= 5):
        print(
            "\tAll permitted accounts have been created.\n \tPlease come back later.\n"
        )
        return None
    username = input("Enter Username: ")
    while (not checkUsername(username)):
        username = input("Enter Username: ")
    password = input("Enter Password:")
    while (not checkPassword(password)):
        password = input("Enter Password: ")
    firstname = input("Enter First Name:")
    while (firstname == None):
        firstname = input("Enter First Name: ")
    lastname = input("Enter Last Name:")
    while (lastname == None):
        lastname = input("Enter Last Name: ")
    userType = int(input(
        "Press 1 for a free standard account\nPress 2 for a ($10/month) Premium account: "))
    while(userType < 1 or userType > 2):
        userType = int(input(
            "Press 1 for a free standard account\nPress 2 for a ($10/month) Premium account: "))

    newUser = User(None)
    newUser.create(username, password, firstname, lastname, userType)
    newUser.createDefaultSettings()
    print("\tAccount Created!\n")
    userNotification = Notification(newUser.getUserId())
    userNotification.newMemberJoined(username, str(newUser.getUserId()))
    main()



def main():
    clearConsole()

    print(
        "Press \"1\" to learn more about how InCollege can help you find a career."
    )
    print("Press \"2\" to connect with an InCollege user.")
    print("Press \"3\" to log in using an existing account.")
    print("Press \"4\" to create a new account.")
    print("Press \"5\" for Useful Links.")
    print("Press \"6\" for InCollege Important Links.")
    loginI = int(input())
    clearConsole()
    if loginI == 1:
        videoScreen()
    elif loginI == 2:
        findSomeoneScreen(User(None))
    elif loginI == 3:
        login()
    elif loginI == 4:
        signup()
    elif loginI == 5:
        usefulLinks(0)
    elif loginI == 6:
        InCollegeImportantLinks(0)
    else:
        print("invalid input")


if __name__ == "__main__":
    main()