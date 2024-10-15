print("Welcome to python pizza Deliveries!")
size=input("What size pizza do you want?S,M Or L:")
pepperoni=input("Do you want pepperoni on your Pizza?Y o N:")
extra_cheese=input("Do you want extra cheese? Y or N:")
bill=0
    # todo:workout which size required.
if size =="s":
    bill=15
elif size =="m":
    bill=20
elif size =="l":
    bill=25
else:
    print("you typed the wrong inputs.")
    
    # todo:workout how much to add to their bill based on their pepperoni choice.
if pepperoni=="y":
    if size=="s":
        bill+=2
    else:
        bill+=3

#todo:work out their final amount based on whether if they want extra cheese>
if extra_cheese =="y":
    bill+=1
    
    
print(f"your total bill is: {bill}")
    