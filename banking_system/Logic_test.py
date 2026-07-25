# import json
# from pathlib import Path


# # 1. This finds the folder you are currently in (the banking_system folder)
# BASE_DIR = Path(__file__).resolve().parent

# # 2. Just add the file name directly! No extra folders needed.
# DATA_FILE_PATH = BASE_DIR/"userData.json"


# def read_user_data():
#     try:
#         with open(DATA_FILE_PATH, "r") as users:
#                 userDatas = json.load(users)
#                 return userDatas
#     except FileNotFoundError:
#         print("⚠️ No database file found.")


# all_users = read_user_data()

# test = str(input("Enter username: "))

# for key, value in all_users.items():

#     if test in value["user_name"]:
#         print("Success")
#         break
#     else:
#         print("fail")

# newDepositeRiel = input("Enter amount of deposite in Riel (Can be a '0'): ")
# if (type(newDepositeRiel) == str) or float(newDepositeRiel) < 0:

#     print("Invaild input")
# else:
#     print("Passed")

while True:
        print("-------------------------------------------------------")
        print("Accepted email format")
        print("Example: smith232@gamil.com")
        print("SHit")
        print("---------------------------------------------------------")
        newEmail = input("Enter your email to link with your account: ")
        if "@" in newEmail and newEmail.endswith("@gmail.com") and newEmail[:newEmail.index("@")] != "":
            print("GOOD")
            break
        else:
            print("Invaild email")
            continue