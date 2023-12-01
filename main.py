import sqlite3
import os
from Library.student import Student


def clearConsole():
    os.system('clear')


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

def optionsScreen(loggedInUser: User):
    clearConsole()
  
    job = Job()

    print("\n\tOptions Screen")
    print("Select an option:")
    print("\t1: Search for a Job")
    print("\t2: Find someone you know")
    print("\t3: Send a message to someone")
    print("\t4: Learn a new skill")
    print("\t5: for Useful Links.")
    print("\t6: for InCollege Important Links.")
    print("\t7: Show my network")
    friend = Friend(loggedInUser.getUserId())
    friendInvites = friend.getInvites()
    print("\t8: You have", len(friendInvites), "new friend invites")
    print("\t9: View my profile")
    message = Message(loggedInUser.getUserId())
    messageList = message.getMessages()
    if(len(messageList) > 0):
        print("\t10: You have messages waiting for you")
    else:
        print("\t10: No new messages.")

    deletedJobs = notifications.appliedJobDeleted(loggedInUser.getUserId())
    job.removeApplication(loggedInUser.getUserId())

    if (deletedJobs):
        for job in deletedJobs:
            print("\tA job that you applied for has been deleted: " + str(job))
    selection = int(input("\t0: Log out\n"))
    clearConsole()
    if selection == 1:
        jobScreenList(loggedInUser)
    elif selection == 2:
        findSomeoneScreen(loggedInUser)
    elif selection == 3:
        messagingScreen = MessagingScreen(loggedInUser.getUserId())
        messagingScreen.messageList()
        optionsScreen(loggedInUser)
    elif selection == 4:
        skillsScreen(loggedInUser)
    elif selection == 5:
        usefulLinks(loggedInUser)
    elif selection == 6:
        InCollegeImportantLinks(loggedInUser)
    elif selection == 7:
        showMyNetworkScreen(loggedInUser)
    elif selection == 8:
        acceptInvitesScreen(loggedInUser)
    elif selection == 9:
        profileScreen = ProfileScreen(loggedInUser)
        profileScreen.render()
        optionsScreen(loggedInUser)
    elif selection == 10:
        messagingScreen = MessagingScreen(loggedInUser.getUserId())
        messagingScreen.viewIncomingMessages(messageList)
        optionsScreen(loggedInUser)
    elif selection == 11:
        optionsScreen(loggedInUser)
    elif selection == 0:
        main()

def login():
    clearConsole()
    print("\n\tLogin Screen")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    tempUser = Student(None)
    student = tempUser.findOneByUsername(username)

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
    

    print("Press any key to login")
    input()
    login()

if __name__ == "__main__":
    main()