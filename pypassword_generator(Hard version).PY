import random

# Declaring a list of lowercase letters (you can add uppercase if needed)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Declaring a list of numeric digits
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Declaring a list of special symbols
symbols = ['#', '@', '!', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to PyPassword Generator!")
choose_letter = int(input("How Many Letters would you like in your Password?\n"))
choose_number = int(input("How Many numbers would you like in your Password?\n"))
choose_symbol = int(input("How Many Symbols would like in your Password?\n"))
password_list = []
for char in range(0, choose_letter):
    password_list.append(random.choice(letters))
for char in range(0, choose_number):
    password_list.append(random.choice(numbers))
for char in range(0, choose_symbol):
    password_list.append(random.choice(symbols))

# Shuffling the password list to randomize the order of letters, numbers, and symbols
random.shuffle(password_list)

# Initializing an empty string to store the final password
password = ""

# Concatenating all the characters from the shuffled password list into a single string
for char in password_list:
    password += char
    
# Displaying the final strong password to the user
print("Your Strong Password:", password)
