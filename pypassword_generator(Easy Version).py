# Easy Version
import random
# Declaring a letter
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Declaring a number
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Declaring a symbols
symbols=['#', '@', '!', '$', '%', '^', '&', '*', '(', ')']
# main code
print("Welcome to PyPassword Generator!")
choose_letter=int(input("How Many Letters would you like  in your Password?\n"))
choose_number=int(input("How Many number would you like in your Password?\n"))
choose_symbol=int(input(f"How Many Symbols would like in your Password?\n"))

password=" "
for char in range(0,choose_letter):
  password+=random.choice(letters)
  
for char in range(0,choose_number):
   password+=random.choice(numbers)
   
for char in range(0,choose_symbol):
  password+=random.choice(symbols)
  
print("your password is:",password)