#Card Creator Generator
import os
import datetime

#date format
datetime.datetime.today()
date_now = (datetime.datetime.today().strftime('_%Y-%m-%d_%Hh%M'))

#Menu
i=0
while i < 1:
    os.system("cls")
    print("|-------------------------|")
    print("| CARD CREATOR by Eidknab |")
    print("|-------------------------|")
    print("https://github.com/Eidknab/")
    print("")
    website = input("Input  Website:_")
    password = input("Input Your Password:_")
    your_mail = input("Input Your Mail:_")
    your_id = input("Input Your ID:_")
    #txt part
    txt_file = website + date_now
    fichier = open(txt_file + ".txt", "w")
    fichier.write(txt_file + "\nWebsite: " + website + "\nUser ID: " + your_id + "\nEmail: " + your_mail + "\nPassword: " + password)
    fichier.close()
    print("\nInformations Have Been Saved in " + txt_file + ".txt")
    print("Don't Forget to Secure the Data Now !")
    key = input("\nNew Card ? (y or n)")
    if key == "y" or key == "Y":
        os.system("cls")
    else:
        i = i + 1



     
