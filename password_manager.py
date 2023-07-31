# import os
# current_directory = os.getcwd()
# print(current_directory)
import pandas as pd

print("WELCOME TO THE PASSWORD MANAGER!")
quest = input("Input the password to disencrypte ")


def view():
    pass

def add():
    with open("tolu.csv",'a') as f:
        data = pd.DataFrame(columns=['Name', 'Password'])
        name = input("Enter your Acount name: ")
        password = input("Enter your Password: ")
        data = data._append({
        'Name': name,
        'Password': password,
        }, ignore_index=True)
        f.write(name +"-"+ password)
        data = pd.DataFrame(columns=['Name', 'Password'])
        print("Information has been saved into tolu.csv")



while True:
    quest_2 = str(input("Do you want to view already existing passwords('v' to view) or Add to your passwords('a' for add)?(click q to quit) ").lower())
    if quest_2 == "v":
        view()
    elif quest_2 == "a":
        add()
    elif quest_2 == "q":
        break
    else:
        print("INVALID INPUT!")
        continue




