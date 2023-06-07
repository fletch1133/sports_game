print("Welcome to my sports quiz")

playing = input("Do you want to play this game, bro? ")

if playing != "yes":
    quit()

print("Okay! Lets play :)")

answer = input("What team did Bill Russel play for? ")
if answer == "Celtics":
    print("You're right, bud!") 
else:
    print("You are incorrect, sir! ")

answer = input("What team did Kobe Bryant play for? ")
if answer == "Lakers":
    print("Wow, you are one smart cookie!") 
else:
    print("Nah, son :( ")

answer = input("What team has the most combined NFL Championships? ")
if answer == "Packers":
    print("You must be an Aaron Rodgers hater these days, huh?") 
else:
    print("Up your NFL knowledge, sonny! ")

answer = input("What team went undefeated in the NFL? ")
if answer == "Dolphins":
    print("Awesome job!") 
else:
    print("You better hit the history books! ")