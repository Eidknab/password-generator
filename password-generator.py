#pw generator
#10
numbers = ["0","1","2","3","4","5","6","7","8","9"]
#27
caracters_lowercase = ["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n"]
#27
caracters_uppercase = ["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]
#30
symbols = [" ","!","#","$","%","(",")","*","+",",","-",".","/",":",";","<",">","=","?","@","[","]","^","_","`","{","}","|","~"]

#Menu
print("PW GENERATOR Build 1")
print("")
print("1. Generate my password")
print("0. Quit")
print("")

#Input
user_answer = input("Type a value:_")


if user_answer == "0":
	pass
elif user_answer == "1":
	print("How many caracters ?")
	caracters_number = input("Type a value:_")
	print("Use Symbols ? y / n")
	symbols_yn = input("Type a value:_")
	pass
else:
	pass
