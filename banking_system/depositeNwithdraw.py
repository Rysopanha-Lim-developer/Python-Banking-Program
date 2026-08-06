# Future update:


import time
import user_account


def deposite_withdraw_money(username):
    isRunning = True
    print("<<<<<Deposite and Withdraw>>>>>")
    print("====================")
    print("Enter 1 for deposite")
    print("====================")
    print("Enter 2 for withdraw")
    print("====================")
    time.sleep(0.5)
    while True:
        try:
            actions = int(input(">>>>>Choose an action:"))
            match actions:
                case 1:
                    deposite_function(username)
                case 2:
                    withdraw_function(username)
                case _:
                    print("Invaild input")
                    continue
        except ValueError:
            print("Invaild input")
            continue


def deposite_function(username):
    isRunning = True
    user_account.show_money_inAcc(username)

    while isRunning:
        try:
            deposite = float(input(">>>>>Enter amount for deposite: "))
            if deposite >= 0:
                newbalance = user_account.all_users[username]["balance"] + deposite
                user_account.json_file_balance_update(username, newbalance)
                time.sleep(2)
                print(f"<----------You successfuly deposite ${float(deposite)} to your account------------>")
                print(f"Your current balance is ${user_account.all_users[username]['balance']}")
                isRunning = False
            else:
                print("Invaild input please enter positve value")
                continue
        except ValueError:
            print("Invaild input, please try again.")
            continue


def withdraw_function(username):
    isRunning = True
    user_account.show_money_inAcc(username)

    while isRunning:
        try:
            withdraw = float(input(">>>>>Enter amount for withdraw: "))
            if withdraw >= 0:
                newbalance = user_account.all_users[username]["balance"] - withdraw
                if newbalance < 0:
                    time.sleep(2)
                    print("Insuffficient balance!!")
                    print(f"Your current balance is ${user_account.all_users[username]['balance']}")
                else:
                    user_account.json_file_balance_update(username, newbalance)
                    time.sleep(2)
                    print(f"<----------You successfuly withdraw ${float(withdraw)} from your account------------>")
                    print(f"Your current balance is ${user_account.all_users[username]['balance']}")
                    isRunning = False
            else:
                print("Invaild input please enter positve value")
                continue
        except ValueError:
            print("Invaild input, please try again.")
            continue





if __name__ == "__main__":
    deposite_withdraw_money("vattana")