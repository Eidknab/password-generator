#Card Creator Generator

#Menu
i = 0
import os
while i < 1:
    os.system("cls")
    from clint.textui import colored, puts
    puts(colored.yellow('|-------------------------|'))
    puts(colored.yellow('| CARD CREATOR by Eidknab |'))
    puts(colored.yellow('|-------------------------|'))
    puts(colored.yellow('https://github.com/Eidknab/'))
    print("")
    website = input("Input  Website:_")
    website = website.lower()
    try:
        website = website.replace("http://", "")
        website = website.replace("https://", "")
        website = website.replace("www.", "")
    except:
        pass
    your_mail = input("Input Your Mail:_")
    your_id = input("Input Your ID:_")
    password = input("Input Your Password:_")
    #txt part
    #date format
    import datetime
    datetime.datetime.today()
    date_now = (datetime.datetime.today().strftime('_%Y-%m-%d_%Hh%M'))
    txt_title = "-------------------------------\n" + "Created" + date_now + "\n" + "-------------------------------"
    fichier = open(website.capitalize() + ".txt", "a")
    fichier.write(txt_title + "\nWebsite: " + website + "\nUser ID: " + your_id + "\nEmail: " + your_mail + "\nPassword: " + password + "\n\n")
    fichier.close()
    print("\nInformations Have Been Saved in " + website + ".txt")
    print("Don't Forget to Secure the Data Now !")
    key = input("\nNew Card ? (y or n)")
    if key == "y" or key == "Y":
        os.system("cls")
    else:
        i = i + 1



     
