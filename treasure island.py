

       
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go?")
road = input("Type 'left' or 'right': ").lower()

if road == "left":
    choose = input("You have come to a lake. There is an island in the middle of the lake. "
                   "Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()
    
    if choose == "wait":
        choose1 = input("You arrive at the island unharmed. There is a house with 3 doors: "
                        "One red, one yellow, and one blue. "
                        "Which colour do you choose? ").lower()
        
        if choose1 == "yellow":
            print("You found the treasure! You win!")
        elif choose1 == "red":
            print("It's a room full of fire. Game over.")
        elif choose1 == "blue":
            print("You enter a room full of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("Attacked by a trout. Game over.")
        
else:
    print("You fell into a hole. Game over.")
