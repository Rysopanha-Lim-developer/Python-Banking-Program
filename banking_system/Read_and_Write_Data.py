import json
from pathlib import Path

# 1. This finds the folder you are currently in (the banking_system folder)
BASE_DIR = Path(__file__).resolve().parent

# 2. Just add the file name directly! No extra folders needed.
DATA_FILE_PATH = BASE_DIR/"userData.json"


def read_user_data():
    try:
        with open(DATA_FILE_PATH, "r") as users:
                userDatas = json.load(users)
                return userDatas
    except FileNotFoundError:
        print("⚠️ No database file found.")


all_users = read_user_data()

def json_file_password_update(username, newpassword):
    try:
        with open(DATA_FILE_PATH, "w") as users:
            newpassword = str(newpassword) 
            all_users[username]['pin'] = newpassword
            json.dump(all_users, users, indent=4)
    except FileNotFoundError:
        print("⚠️ No database file found.")


def json_file_balance_update(username, newbalance):
    try:
        with open(DATA_FILE_PATH, "w") as users:
            all_users[username]['balance'] = newbalance
            json.dump(all_users, users, indent=4)
    except FileNotFoundError:
        print("⚠️ No database file found.")


def json_file_balance_riel_update(username, newbalance):
    try:
        with open(DATA_FILE_PATH, "w") as users:
            all_users[username]['balance_riel'] = newbalance
            json.dump(all_users, users, indent=4)
    except FileNotFoundError:
        print("⚠️ No database file found.")


def json_file_frozen_status(username, newfrozen_state):
    try:
        with open(DATA_FILE_PATH, "w") as users:
            all_users[username]['frozen'] = newfrozen_state
            json.dump(all_users, users, indent=4)
    except FileNotFoundError:
        print("⚠️ No database file found.")


def UploadNewAcc(passed_in_username, passed_in_datas):
    try:
        with open(DATA_FILE_PATH, "w") as dataBase:

            #This will add new key value pair instead of replacing old data
            all_users[passed_in_username] = passed_in_datas
            json.dump(all_users, dataBase, indent=4)

    except FileNotFoundError:
        print("⚠️ No database file found.")