#pw generator
#10
numbers = ["0","1","2","3","4","5","6","7","8","9"]
#27
caracters_lowercase = ["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n"]
#27
caracters_uppercase = ["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]
#30
symbols = [" ","!","#","$","%","(",")","*","+",",","-",".","/",":",";","<",">","=","?","@","[","]","^","_","`","{","}","|","~"]

def generate (param0, param1, param2, param3, param4):
	i = param0
	pw = "test"
	return pw
	pass

#Menu
print("PW GENERATOR Build 2")
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
	print(generate(caracters_number, numbers, caracters_lowercase, caracters_uppercase, symbols))
	pass
else:
	pass
