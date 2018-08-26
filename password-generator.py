#Password Generator

#enter your mail here for automated file writing
your_mail = ""
#enter you id here for automated file writing
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
i=0
print("PASSWORD GENERATOR by Eidknab")
print("")
caracters_number = int(input("How Many Characters?_"))
password = generate(caracters_number, character_list)
print(password)
print("Password Copied to Clipboard")
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
print("Informations Have Been Saved in " + txt_file + ".txt")
print("Don't Forget to Secure the Data Now !")


     
