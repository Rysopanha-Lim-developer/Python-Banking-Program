# Future update:

import time
import user_account


def deposite_withdraw_money(username):
    print("<<<<<Deposite and Withdraw>>>>>")
    print("====================")
    print("Enter 1 for deposite")
    print("====================")
    print("Enter 2 for withdraw")
    print("====================")
    time.sleep(0.5)
    try:
        actions = int(input(">>>>>Choose an action:"))
        match actions:
            case 1:
                deposite_function(username)
            case 2:
                withdraw_function(username)
            case _:
                print("Invaild input")
                deposite_withdraw_money(username)
    except ValueError:
        print("Invaild input")
        deposite_withdraw_money(username)


def deposite_function(username):
    user_account.deposite_money_inAcc(username)

    try:
        deposite = float(input(">>>>>Enter amount for deposite: "))
        if deposite >= 0:
            newbalance = user_account.all_users["userDataList"][username]["balance"] + deposite
            user_account.json_file_balance_update(username, newbalance)
            time.sleep(2)
            print(f"<----------You successfuly deposite ${float(deposite)} to your account------------>")
            print(f"Your current balance is ${user_account.all_users["userDataList"][username]["balance"]}")
        else:
            print("Invaild input please enter positve value")
            deposite_function(username)
    except ValueError:
        print("Invaild input, please try again.")
        deposite_function(username)


def withdraw_function(username):
    user_account.deposite_money_inAcc(username)

    try:
        withdraw = float(input(">>>>>Enter amount for deposite: "))
        if withdraw >= 0:
            newbalance = user_account.all_users["userDataList"][username]["balance"] - withdraw
            if newbalance < 0:
                time.sleep(2)
                print("Insuffficient balance!!")
                print(f"Your current balance is ${user_account.all_users["userDataList"][username]["balance"]}")
            else:
                user_account.json_file_balance_update(username, newbalance)
                time.sleep(2)
                print(f"<----------You successfuly withdraw ${float(withdraw)} from your account------------>")
                print(f"Your current balance is ${user_account.all_users["userDataList"][username]["balance"]}")
        else:
            print("Invaild input please enter positve value")
            withdraw_function(username)
    except ValueError:
        print("Invaild input, please try again.")
        withdraw_function(username)




if __name__ == "__main__":
    deposite_withdraw_money("vattana")