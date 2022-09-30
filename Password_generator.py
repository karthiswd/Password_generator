import random

Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z']
Symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

print("Create your password here Welcome!")
nr_letters = int(input("How many letter would you like? \n"))
nr_symbols = int(input("How many symbol would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(Letters)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(Symbol)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char
print(f"Your password is: {password}")
