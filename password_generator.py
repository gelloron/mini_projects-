import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = "1234567890"
symbols = "!@#$%^&*()_+|?:><.,{}[]"
all_of_characters = lower + upper + num + symbols
while True:
    print("please select an option :\n\t 1) create a password  \n\t 2) exit  ")
    choice = input("your choice :> ")
    if choice == "1":
        length = int(input("tell us the length of your password:> "))
        password = "".join((random.sample(all_of_characters, length)))
        print(f"your password is {password}")
        print('*' * 60 + "\n")
    elif choice == "2":
        print("thanks for your time and goodbye:)  ")
        print('*' * 60 + "\n")
        break
    else:
        print("!!!!! INCORRECT INPUT PLEASE ENTER THE CORRECT INPUT !!!!!")
        print('*' * 60 + "\n")
