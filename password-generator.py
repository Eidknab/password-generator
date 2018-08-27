#Password Generator

#enter your mail here for automated file writing
# bankdie@protonmail.com
your_mail = ""
#enter you id here for automated file writing
# Eidknab
your_id = ""

#88 characters
character_list = ["%","(",")"," ","!","#","$","*","+",",","-",",","/",":",";","=","?","@","[","]","^","_","0","`","{","}","~","1","2","3","4","5","6","7","8","9","a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n","A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]

#password generation fonction
def generate(param0, param1):
    i = 1
    pw = ""
    from random import randrange
    while i < param0+1:
        n = randrange(0, 88)
        pw = pw + character_list[n]
        i += 1
    copy2clip(pw)
    return pw

import subprocess
#write clipboard fonction
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

import datetime
#date format
datetime.datetime.today()
date_now = (datetime.datetime.today().strftime('_%Y-%m-%d_%Hh%M'))

#Menu
import os
os.system("cls")
print("|-------------------------------|")
print("| PASSWORD GENERATOR by Eidknab |")
print("|-------------------------------|")
print("https://github.com/Eidknab/")
print("")
i = 0
caracters_number = input("How Many Characters?_")
caracters_number = int(caracters_number)
password = generate(caracters_number, character_list)
print("\nYour password is:", password, "\n")
print("Password Copied to Clipboard\n")
website = input("Enter Website:_")
if your_mail == "":
    your_mail = input("Enter Your Mail:_")
    pass
else:
    pass
if your_id == "":
    your_id = input("Enter Your ID:_")
    pass
else:
    pass
#txt part
txt_file = website + date_now
fichier = open(txt_file + ".txt", "w")
fichier.write(txt_file + "\nWebsite: " + website + "\nUser ID: " + your_id + "\nEmail: " + your_mail + "\nPassword: " + password)
fichier.close()
print("\nInformations Have Been Saved in " + txt_file + ".txt")
print("Don't Forget to Secure the Data Now !")


     
