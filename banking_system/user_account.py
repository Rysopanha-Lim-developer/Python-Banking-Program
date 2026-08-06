# Future update:


import Read_and_Write_Data
import time
import secrets




def userInput_function():
    while True:
        usernameInput = input(">>>>>Enter your username: ").lower()
        if userAutentication(usernameInput):
            continue
        else:
            return usernameInput


def userAutentication(username): 
    max_attempts = 5   
    if (username in Read_and_Write_Data.all_users) and (not Read_and_Write_Data.all_users[username]["frozen"]):
        for i in range(max_attempts): 
            passwordInput = input(">>>>>Enter 6 digits PIN: ")
            
            if (str(passwordInput) == Read_and_Write_Data.all_users[username]['pin']):
                greeting_user(username)
                break
            else:
                max_attempts -=1
                if max_attempts > 0:
                    print(f"Wrong password! You have {max_attempts} more try...")
                    continue
                elif max_attempts <= 0:
                    print("Your account has been lock")
                    if reset_password_restriction(username):
                        return True
                    return new_password_verification(username)
    else:
        print("Username Not available!")
        print("OR your account has been locked!")
        return True


def resetPassword(username):
    while True:
        newPassword = input(">>>>>Enter new 6 digits PIN: ")
        if len(newPassword) == 6 and newPassword.isdigit():
            Read_and_Write_Data.json_file_password_update(username, newPassword)
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
        if verify_email == Read_and_Write_Data.all_users[username]["email"]:
            return confirm_OTP(username)
        else:
            print("Wrong email try again...")
            continue


def new_password_verification(username):
    max_attempts = 5   
    for i in range(max_attempts): 
        passwordInput = input(">>>>>Enter 6 digits PIN: ")
        
        if (str(passwordInput) == Read_and_Write_Data.all_users[username]['pin']):
            greeting_user(username)
            break
        else:
            max_attempts -=1
            if max_attempts > 0:
                print(f"Wrong password! You have {max_attempts} more try...")
                continue
            elif max_attempts <= 0:
                Read_and_Write_Data.json_file_frozen_status(username, True)
                print("Your account has been frozen...")
                print("Please contact our support team for account recovery.")
                print("-----------------------")
                print("Login to other account?")
                return True


def confirm_OTP(username):
    otp = ''.join(str(secrets.randbelow(10)) for _ in range(6))
    print(f"This is your OTP {otp}")

    max_attempts = 5
    for i in range(max_attempts):
        print(f"You have {max_attempts} left")
        otp_input = input("Enter your OTP: ")
        if otp_input == otp:
            resetPassword(username)
            return False
        max_attempts -= 1
        print("Wrong code please try again")
    if max_attempts <= 0:
        Read_and_Write_Data.json_file_frozen_status(username, True)
        print("You have reached the maximum attempts")
        print("Your account has been frozen...")
        print("Please contact our support team for account recovery.")
        print("-----------------------")
        print("Login to other account?")
        return True



def greeting_user(username):
    print("==========================")
    print(f"Welcome {username}")
    print("==========================")


def show_money_inAcc(username):
    print(f"<----------You currently have ${Read_and_Write_Data.all_users[username]['balance']}------------>")
    print(f"<----------You currently have {Read_and_Write_Data.all_users[username]['balance_riel']} Riel------------>")


def return_back_to_menu():
    time.sleep(1)
    print("==========================")
    print("To return to the main menu")
    print("==========================")
    while True:
        return_back = input("Enter 'R' to return: ").lower()
        if return_back == "r":
            return True
        else:
            print("Invalid input. Please try again")
            continue




if __name__ == "__main__":
    userAutentication("panha168")