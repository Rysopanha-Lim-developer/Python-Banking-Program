# TODo
# 1. Create a class that take in users data for acc creation
# 2. Create a class for dollar acc creation
# 3. Create a class for riel acc creation

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

def UploadNewAcc(a):
    try:
        with open(DATA_FILE_PATH, "w") as dataBase:
            writeNewUser["userDataList"] = a
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
        self.uniqueId = str(uuid.uuid4())[:8]


    def CreateNewAcc(self):
        print(self.uniqueId)
        return {self.uniqueId:{
            "user_name":self.username,
            "pin": self.pin,
            "email": self.email,
            "balance": self.deposite,
            "balance_riel": self.depositeRiel
        }}

def AccCreation():
    print("========================")
    print("New account registration")
    print("========================")

    newUsername = input("Enter your username: ")
    newPassword = input("Enter your 6 digits pin: ")
    newEmail = input("Enter your email: ")
    newDollar = input("Enter amount of deposite in Dollar (Can be a '0'): ")
    newRiel = input("Enter amount of deposite in Riel (Can be a '0'): ")

    newClient = CreateAcc(newUsername, newPassword, newEmail, newDollar, newRiel)
    a = newClient.CreateNewAcc()

    UploadNewAcc(a)



if __name__ == "__main__":
    AccCreation()