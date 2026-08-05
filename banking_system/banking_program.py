# Future update:
# 4. Create real UI PyQt5 GUI
# 5. Find new ways to store users datas

import time
import user_account
import depositeNwithdraw
import transfer
import money_exchange
import new_user
# from PyQt5.QtWidgets import QApplication, QMainWindow


def ui():
    print("==========================")
    print("Welcome to World Wide Bank")
    print("==========================")

    print("======================================")
    print("Enter 0 to Create new account")
    print("Enter 1 to see view your balance.")
    print("Enter 2 to Deposite/Withdraw money")
    print("Enter 3 to Transfer money")
    print("Enter 4 to Exchange money")
    print("Enter 5 to Exit the application.")
    print("======================================")
    time.sleep(0.5)


def choices():
    while True:
        try:
            choice = int(input(">>>Choose your actions: "))
            if 0 <= choice <= 5:
                return choice
            print("Invalid input. Please try again")
        except ValueError:
            print("Invalid input. Please try again")


app_run = True
while app_run:
    ui()
    choice = choices()      
    match choice:
        case 0:
            new_user.AccCreation()
            print("Your account has been created successfully")
            print("Thank you for choose our bank")

            user_account.return_back_to_menu()
            print("Returning to main menu...")
            time.sleep(5)
        case 1:
            users = user_account.userInput_function()
            
            user_account.deposite_money_inAcc(users)

            user_account.return_back_to_menu()
            print("Returning to main menu...")
            time.sleep(5)
        case 2:
            users = user_account.userInput_function()

            depositeNwithdraw.deposite_withdraw_money(users)

            user_account.return_back_to_menu()
            print("Returning to main menu...")
            time.sleep(5)
        case 3:
            users = user_account.userInput_function()

            transfer.money_transfer(users)

            user_account.return_back_to_menu()
            print("Returning to main menu...")
            time.sleep(5)
        case 4:
            users = user_account.userInput_function()

            money_exchange.money_convertion(users)

            user_account.return_back_to_menu()
            print("Returning to main menu...")
            time.sleep(5)
        case 5:
            print("Exiting the program...")
            time.sleep(3)
            app_run = False
        case _:
            print("Invaild choise")
            app_run