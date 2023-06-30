#choose your adventure

name = input('Type your name: ')
print("Welcome", name, "on this extraordinary adventure!!!")

answer = input("You are on a football field, you can go right or left. Which way you going? ").lower()

if answer == "left":
    answer = input("You come to a lockerroom. You can walk around it or enter it. Type walk to walk around or type enter to enter: ")
    
    if answer == "walk":
        print("You walked around the the lockers. A python killed you and you lose!")
    elif answer == "enter":
        print("you got beat to death by the jocks! You lose")
    else:
        print('This is not valid. You lost!')

elif answer == "right":
    answer = input("You come to the parking lot. It looks like a sinkhole is going to occur. Do you want to cross it or head back on around (cross/back) ? ")

    if answer == "back":
        print("You walked back and got hit by a linebacker giving you a brain bleed and killing your sorry butt!! ")
    elif answer == "cross":
        answer = input("You are now in the middle of a school fight! Do you fight (yes/no)? ")

        if answer == "yes":
            print("You fight and win the schools respect! ")

        elif answer == "no":
            print("You dont fight and still get beat up! You lost sucker! ")

    else:
        print('This is not valid. You lost!')

else:
    print('This is not valid. You lost!')

print("Thank you for playing this crazy new game, " + name)
