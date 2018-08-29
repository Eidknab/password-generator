#Password Generator

#enter your mail & userid here for automated file writing
# exemple: 
#your_mail = "mymail@hello.com"
#your_id = "myuserid"
your_mail = ""
your_id = ""

#88 characters
character_list = ["@","-","_","=","$","£","*","?",".","/","!",":",">","%","0","`","{","}","0","1","2","3","4","5","6","7","8","9","a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n","A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]
# may have some compatibility problems on some site  
# "%","(",")"," ","!","#","$","*","+",",","-",",","/",":",";","=","?","@","[","]","^","_","`","{","}","~",
#password generation fonction
def generate(param0, param1):
    i = 1
    pw = ""
    from random import randrange
    while i < param0+1:
        n = randrange(0, 76)
        pw = pw + character_list[n]
        i += 1
    copy2clip(pw)
    return pw

#write clipboard fonction
import subprocess
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

#Menu
import os
os.system("cls")
print("|-------------------------------|")
print("|      PASSWORD GENERATOR       |")
print("|-------------------------------|")
print("")
print("")
i = 0 
while i < 1:
	caracters_number = input("How Many Characters?_")
	try:
		caracters_number = int(caracters_number)
		i = i + 1
	except:
		print("Input Error")
password = generate(caracters_number, character_list)
print("\nYour password is:", password, "\n")
print("Password Copied to Clipboard\n")
website = input("Enter Website:_")
website = website.lower()
try:
	website = website.replace("http://", "")
	website = website.replace("https://", "")
	website = website.replace("www.", "")
except:
	pass
if your_mail == "":
    your_mail = input("Enter Your Mail:_")
else:
	print("Mail Found in Memory: " + your_mail)
if your_id == "":
    your_id = input("Enter Your ID:_")
    print("/?\ For better automation, your mail and your userID are editable in .py file (line 3-8).")
else:
	print("User ID Found in Memory: " + your_id)
#date format
import datetime
datetime.datetime.today()
date_now = (datetime.datetime.today().strftime(' %Y-%m-%d %Hh%M'))
#txt part
txt_title = "-------------------------------\n" + "Created" + date_now + "\n" + "-------------------------------"
fichier = open(website.capitalize() + ".txt", "a")
fichier.write(txt_title + "\nWebsite: " + website + "\nUser ID: " + your_id + "\nEmail: " + your_mail + "\nPassword: " + password + "\n\n")
fichier.close()
print("\nInformations Have Been Saved in " + website + ".txt")
print("Don't Forget to Secure the Data Now !")

     
