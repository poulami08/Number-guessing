# We are going to write a program that generates a random number and asks the user to guess it.

# If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please”.

# When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

import random

print("                                                  ****** GUESS THE NUMBER *******                  ")
print(" ")
rand = random.randint(1,101)
i=1
while(i>0):
    print("User - guess the number")
    m=int(input())
    i=i+1 
    if m <=100 and m>=1:
        if rand == m:
            print("Right answer")
            print("The number of guesses the player used to arrive at the number is " + str(i-1))
            print(" ")

            print("                                                         ***** GAME OVER ******                 ")
            break
        elif m>rand:
                print("Lower number please")
        elif m<rand:
            print("higher number please")
    else:  
        print("Option not found , please try again")    

with open("python_projects/guess_the_number/hiscore.txt", "r") as f:
     hiscore = int(f.read())
     

if(i<hiscore):
    print("you have just broken the high score !")
    with open("python_projects/guess_the_number/hiscore.txt", "w") as f:
        f.write(str(i-1))      
    