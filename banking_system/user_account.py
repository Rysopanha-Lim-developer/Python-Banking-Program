# Future update:
# 1. Separate the re-enter password to make it appear before all entry
# 2. Add rate limit to email verification
# 3. use "for key, value in database.items()" to store both unique key and all value in it
# 4. create a variable to store unique id after successful login 
# 5. remove all ["UserDataList"] 



import json
from pathlib import Path
import time
import secrets

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


def userInput_function():
    while True:
        usernameInput = input(">>>>>Enter your username: ").lower()
        if userAutentication(usernameInput):
            continue
        else:
            return usernameInput


def userAutentication(username): 
    max_attempts = 5   
    if username in all_users:
        for i in range(max_attempts): 
            passwordInput = input(">>>>>Enter 6 digits PIN: ")
            
            if (str(passwordInput) == all_users[username]['pin']):
                greeting_user(username)
                break
            else:
                max_attempts -=1
                if max_attempts > 0:
                    print(f"Wrong password! You have {max_attempts} more try...")
                    continue
                elif max_attempts <= 0:
                    print("Your account has been lock")
                    reset_password_restriction(username)
                    return new_password_verification(username)
    else:
        print("Username Not available!")
        return True


def resetPassword(username):
    while True:
        newPassword = input(">>>>>Enter new 6 digits PIN: ")
        if len(newPassword) == 6 and newPassword.isdigit():
            json_file_password_update(username, newPassword)
            print("=====================")
            print(" PIN has been reset")
            print("=====================")
            
            return False
        else:
            print("Fail to reset PIN!")
            continue


def reset_password_restriction(username):
    while True:
        print("==============================================")
        print("Please verify your email for account recovery.")
        print("==============================================")
        verify_email = input("Enter your email here: ")
        if verify_email == all_users[username]["email"]:
            return confirm_OTP(username)
        else:
            print("Wrong email try again...")
            continue


def new_password_verification(username):
    max_attempts = 5   
    for i in range(max_attempts): 
        passwordInput = input(">>>>>Enter 6 digits PIN: ")
        
        if (str(passwordInput) == all_users[username]['pin']):
            greeting_user(username)
            break
        else:
            max_attempts -=1
            if max_attempts > 0:
                print(f"Wrong password! You have {max_attempts} more try...")
                continue
            elif max_attempts <= 0:
                print("Your account has been frozen...")
                print("Please contact our support team for account recovery.")
                print("-----------------------")
                print("Login to other account?")
                return True


def confirm_OTP(username):
    max_attempts = 5
    confirming = True
    otp = ''

    for i in range (6):
        opt_fragment = secrets.randbelow(10)
        otp += str(opt_fragment)

    print(f"This is your OTP {otp}")

    while confirming:
        otp_input = input("Enter your OTP: ")
        for i in range(max_attempts):
            if max_attempts < 0:
                confirming = False
                return True
            
            if otp_input == otp:
                resetPassword(username)
                confirming = False
                break
            else:
                max_attempts -= 1
                print("Wrong code please try again in 30s")
                time.sleep(30)
                continue



def greeting_user(username):
    print("==========================")
    print(f"Welcome {username}")
    print("==========================")


def deposite_money_inAcc(username):
    print(f"<----------You currently have ${all_users[username]["balance"]}------------>")


def return_back_to_menu():
    time.sleep(1)
    print("==========================")
    print("To return to the main menu")
    print("==========================")
    return_back = input("Enter 'R' to return: ").lower()
    if return_back == "r":
        return True
    else:
        print("Invalid input. Please try again")
        return_back_to_menu()




if __name__ == "__main__":
    userAutentication("panha168")