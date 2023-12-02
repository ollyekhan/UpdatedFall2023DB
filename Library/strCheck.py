def pwValidation(str):
    return checkIfStrContainsUpperChar(str) and checkIfStrContainsDigit(str) and checkIfStrContainsSpecialChar(str)

def checkIfStrContainsUpperChar(str):
    for char in str:
        if char.isupper():
            return True
    return False


def checkIfStrContainsDigit(str):
    for char in str:
        if char.isdigit():
            return True
    return False

def checkIfStrContainsSpecialChar(str):
    specialChars = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_"]
    for char in str:
        if char in specialChars:
            return True
    return False