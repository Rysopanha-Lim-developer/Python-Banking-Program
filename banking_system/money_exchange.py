# Future update:

import Read_and_Write_Data
import time

#Exchange rate 1$ = 4100Riel

def money_convertion(username):
    print("<<<<<Money exchange>>>>>")
    time.sleep(0.5)
    exchange_choices(username)


def exchange_choices(username):
    print("==========================")
    print("Enter 1 for Riel to Dollar")
    print("Enter 2 for Dollar to Riel")
    print("==========================")
    try:
        choice = int(input(">>>Choose your actions: "))
        if choice == 1:
            riel_to_dollar(username)
        elif choice == 2:
            dollar_to_riel(username)
        else:
            print("Invaild input. Please try again") 
            exchange_choices(username)
    except ValueError:
        print("Invaild input. Please try again") 
        exchange_choices(username)


def dollar_to_riel(username):
    dollar = Read_and_Write_Data.all_users[username]["balance"]
    riel = Read_and_Write_Data.all_users[username]["balance_riel"]

    while True:
        dollar_from = input("Enter the amount for exchange: ")
        try:
            if 0 <= float(dollar_from) <= dollar:
                exchaged_money = round(riel + (float(dollar_from)*4100), 2)
                new_dollar = dollar - float(dollar_from)
                Read_and_Write_Data.json_file_balance_update(username, new_dollar)
                Read_and_Write_Data.json_file_balance_riel_update(username, exchaged_money)
                print(f"Successfully exchange ${dollar_from} to Riel")
                return False
            else:
                print("Insufficient balance.")
                continue
        except ValueError:
            print("Invaild input")
            continue


def riel_to_dollar(username):
    dollar = Read_and_Write_Data.all_users[username]["balance"]
    riel = Read_and_Write_Data.all_users[username]["balance_riel"]

    while True:
        riel_from = input("Enter the amount for exchange: ")
        try:
            if 0 <= float(riel_from) <= riel:
                exchaged_money = round(dollar + (float(riel_from)/4100), 2)
                new_riel = riel - float(riel_from)
                Read_and_Write_Data.json_file_balance_update(username, exchaged_money)
                Read_and_Write_Data.json_file_balance_riel_update(username, new_riel)
                print(f"Successfully exchange {riel_from} Riel to Dollar")
                return False
            else:
                print("Insufficien balance.")
                continue
        except ValueError:
            print("Invaild input")
            continue


if __name__ == "__main__":
    money_convertion("panha")