import os
import time
while True:
    wanna_continiue = input("do you want to start the timer? (y/n):> ")
    if "y" in wanna_continiue.lower():
        hour = int(input("enter hour(s):> "))
        minute = int(input("enter minute(s):> "))
        second = int(input("enter second(s):> "))
        total = hour * 3600 + minute * 60 + second
        print("timer is starting now .....")
        time.sleep(1)
        while total>=1:
            print(total)
            total-=1
            time.sleep(1)
            os.system("cls")
        print("TIMER STOP")
    elif"n" in wanna_continiue.lower():
        print("have a good day :) ")
        break
    else:
        print("PLEASE ENTER y FOR yes AND n FOR no ")
