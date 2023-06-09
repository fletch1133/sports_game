print("Welcome to my sports quiz")

playing = input("Do you want to play this game, bro? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :)")
score = 0

answer = input("What team did Bill Russel play for? ")  ##Could use .lower() here to automatically substitute for lower case instead of adding it to the variable name
if answer.lower() == "celtics":
    print("You're right, bud!") 
    score += 1    ## same as doing score = score + 1
else:
    print("You are incorrect, sir! ")

answer = input("What team did Kobe Bryant play for? ")
if answer.lower() == "lakers":
    print("Wow, you are one smart cookie!")
    score += 1
else:
    print("Nah, son :( ")

answer = input("What team has the most combined NFL Championships? ")
if answer.lower() == "packers":
    print("You must be an Aaron Rodgers hater these days, huh?")
    score += 1 
else:
    print("Up your NFL knowledge, sonny! ")

answer = input("What team went undefeated in the NFL? ")
if answer.lower() == "dolphins":
    print("Awesome job!")
    score += 1
else:
    print("You better hit the history books! ")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%")