# Future update:
# 1. Fix accepting negative value (done)

import user_account
import time


def money_transfer(sender):
    print("<<<<<Money transfer>>>>>")
    time.sleep(1)
    while True:
        reciver = input(">>>>>Enter username for reciver: ")
        if sender != reciver and sender in user_account.all_users['userDataList'] and reciver in user_account.all_users['userDataList']:
            transfer_function(sender, reciver)
            break
        else:
            print("Please check the reciver username again.")
            continue


def transfer_function(sender, reciver):
        money_sender = user_account.all_users['userDataList'][sender]['balance']

        while True:
            money_recieve = input(">>>Enter the amout of money to transfer: ")
            time.sleep(1)
            try:
                if float(money_recieve) >= 0:
                    amount_to_send = float(money_recieve)
                    transfer_calculation(sender, money_sender, reciver, amount_to_send)
                    break
                else:
                    print("Invalid input. Please enter a valid number (e.g., 10 or 10.50)")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number (e.g., 10 or 10.50)")
                continue


def transfer_calculation(sender, money_sender, reciver, money_recieve):
    money_left_sender = money_sender - float(money_recieve)
    if money_left_sender >= 0:
        meney_left_reciever = user_account.all_users['userDataList'][reciver]['balance'] + float(money_recieve)
        user_account.json_file_balance_update(sender, money_left_sender)
        user_account.json_file_balance_update(reciver, meney_left_reciever)
        time.sleep(1)
        print(f"You successfully transfered ${meney_left_reciever} to {reciver}")
        user_account.deposite_money_inAcc(sender)
    else:
        print("Insufficient balance.")
        user_account.deposite_money_inAcc(sender)
        transfer_function(sender, reciver)





if __name__ == "__main__":
    money_transfer("panha")