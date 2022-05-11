import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',' n', 'o', 'p', 'q', 'r', 's', 't,' 'u', 'v', 'w', 'x', 'y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
Symbols = ['!','@','#','$','%','&','(',')','*','+']

#This is the password generator
no_letters = int(input("How many letters would you like to have in your password?\n"))
no_symbols = int(input(f"How many symbols would you like to have in your password?\n"))
no_numbers = int(input(f"How many numbers would you like to have?\n"))


random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(Symbols)


Password = letters[0:no_letters] + numbers[0:no_numbers] + Symbols[0:no_symbols]
random.shuffle(Password)
final_password = ''.join(Password)
print(final_password)