name = input("Type your name: ")
print("Welcome",name,"to this adventure")

answer = input("You are on a dirt road,it has come to an end and you can go left or right.Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross.Type walk to walk around or swim to swim accross: ").lower()
    if answer == "swim":
        print("You swim accross and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles,ran out of water and you lost the game.")
    else:
        print("Not a valid option")    
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)").lower()
    
    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You meet a stranger after crossing the bridge, would you like to talk to them? (Y/N)").lower()
        
        if answer == "y":
            print("you talk to the stranger but he stabs you in the stomach. you did not remember what your mumma told you 'never talk to strangers' and you lose!")
        elif answer == "n":
            print("you don't talk to others you are RUDE, you lose!")
        else:print("Not a valid option.You lose!")
    else:print("not a valid option.You lose!")    
else:
    print("Not a valid option. You lose!")