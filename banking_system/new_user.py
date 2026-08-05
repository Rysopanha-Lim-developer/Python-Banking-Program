# TODo


import json
import uuid
from pathlib import Path

# 1. This finds the folder you are currently in (the banking_system folder)
BASE_DIR = Path(__file__).resolve().parent

# 2. Just add the file name directly! No extra folders needed.
DATA_FILE_PATH = BASE_DIR/"userData.json"


def ReadData():
    try:
        with open(DATA_FILE_PATH, "r") as dataBase:
            readedData = json.load(dataBase)
            return readedData

    except FileNotFoundError:
        print("⚠️ No database file found.")


writeNewUser = ReadData()

def UploadNewAcc(passed_in_username, passed_in_datas):
    try:
        with open(DATA_FILE_PATH, "w") as dataBase:

            #This will add new key value pair instead of replacing old data
            writeNewUser[passed_in_username] = passed_in_datas
            json.dump(writeNewUser, dataBase, indent=4)

    except FileNotFoundError:
        print("⚠️ No database file found.")


class GetUsersData:
    def __init__(self, username, pin, email):
        self.username = username
        self.pin = pin
        self.email = email


class CreateAcc(GetUsersData):
    def __init__(self, username, pin, email, deposite, depositeRiel):
        super().__init__(username, pin, email)
        self.deposite = deposite
        self.depositeRiel = depositeRiel
        self.id = str(uuid.uuid4())[:8]
        self.frozen = False


    def CreateNewAcc(self):
        return self.username, {
                                "id"          : self.id,
                                "frozen"      : self.frozen,
                                "pin"         : self.pin,
                                "email"       : self.email,
                                "balance"     : float(self.deposite),
                                "balance_riel": float(self.depositeRiel)
                            }

def AccCreation():
    print("========================")
    print("New account registration")
    print("========================")

    newUsername = NewUsernameCheck()
    newPassword = NewPinCheck()
    newEmail = NewEmailCheck()
    newDollar = NewDepositeDollar()
    newRiel = NewDepositeRiel()

    newClient = CreateAcc(newUsername, newPassword, newEmail, newDollar, newRiel)
    passed_in_username, passed_in_datas = newClient.CreateNewAcc()

    UploadNewAcc(passed_in_username, passed_in_datas)


def NewUsernameCheck():
    while True:
        print("---------------------------------------------------------")
        print("Username must be unique")
        print("Username must be between 7 and 22 characters")
        print("Username mustnot contains any special characters or space")
        print("---------------------------------------------------------")
        newUsername = input("Create your username: ").lower()
        if (not newUsername.isalnum()) or (len(newUsername) < 7 or len(newUsername) > 22):
            continue

        is_duplicate = False
        if newUsername in writeNewUser:
            is_duplicate = True
            break         

        if is_duplicate:
            print("Failed to create username")
            continue          
        else:
            print("Success")
            return newUsername


def NewPinCheck():
    while True:
        newPin = input("Create your 6 digits pin: ")
        if (not newPin.isdigit()) or (len(newPin)<6 or len(newPin)>6):
            print("----------------------------")
            print("PIN must contain only number")
            print("PIN must be 6 digit")
            print("----------------------------")
            continue
        else:
            return newPin


def NewEmailCheck():
    while True:
        print("-------------------------------------------------------")
        print("Accepted email format")
        print("Example: smith232@gmail.com")
        print("---------------------------------------------------------")
        newEmail = input("Enter your email to link with your account: ")
        if ("@" not in newEmail) or (not newEmail.endswith('@gmail.com')) or (newEmail[:newEmail.index("@")] == ""):
            print("Invaild email")
            continue
        else:
            return newEmail


def NewDepositeDollar():
    while True:
        try:
            print("-----------------------------------------------------------------------")
            newDepositeDollar = float(input("Enter amount of deposite in Dollar (Can be a '0'): "))
            if newDepositeDollar < 0:
                print("----------------------------------")
                print("Invaild input")
                print("Deposite must be at least 0 Dollar")
                print("Deposite must be a number")
                print("----------------------------------")
                continue
            else:
                return newDepositeDollar
        except ValueError:
            print("----------------------------------")
            print("Invaild input")
            print("Deposite must be at least 0 Dollar")
            print("Deposite must be a number")
            print("----------------------------------")
            continue


def NewDepositeRiel():
    while True:
        try:
            print("-------------------------------------------------------------------")
            newDepositeRiel = float(input("Enter amount of deposite in Riel (Can be a '0'): "))
            if newDepositeRiel < 0:
                print("----------------------------------")
                print("Invaild input")
                print("Deposite must be at least 0 Riel")
                print("Deposite must be a number")
                print("----------------------------------")
                continue
            else:
                return newDepositeRiel
        except ValueError:
            print("----------------------------------")
            print("Invaild input")
            print("Deposite must be at least 0 Riel")
            print("Deposite must be a number")
            print("----------------------------------")
            continue



if __name__ == "__main__":
    AccCreation()