while True:
    print("welcome to text encryptor :)")
    print("please select a number :\n\t 1) encrypt\n\t 2) decrypt\n\t 3) exit")
    choice = input("your choice :> ")
    if choice == "1":
        # getting a text and encrypting it by using ascii * 2 + 3
        raw_text = input("please enter your text : ")
        encrypted_text = ""
        for c in raw_text:
            x = ord(c) * 2 + 3
            encrypted_text += chr(x)
        print(f"your encrypted text is : {encrypted_text}")
        print('*' * 60 + "\n")

    elif choice == "2":
        # getting a encrypted text and decrypting it by using (ascii - 3 ) / 2
        encrypted_text = input("please enter your encrypted text: ")
        raw_text = ""
        for c in encrypted_text:
            y = (ord(c)-3)//2
            raw_text += chr(y)
        print(f"your decrypted text is :{raw_text}")
        print('*' * 60 + "\n")

    elif choice == "3":
        print("thanks for your time and goodbye:)  ")
        print('*' * 60 + "\n")
        break
    else:
        print("!!!!! INCORRECT INPUT PLEASE ENTER THE CORRECT INPUT !!!!!")
        print('*' * 60 + "\n")
