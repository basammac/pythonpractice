import random
import time

print(

"""
============================================================
****guess the number game****
========================================================
Please enter the integer between 1-50!
"""

)
number = random.randint(1,50)
numberofguesses=0

name=input("enter your name")

print("Hi",name,"I'm thinking of am whole number between 1 to 50 can you guess what it is?")

while (numberofguesses < 8):
 try:
    guess=int(input("Take a guess:"))
    numberofguesses +=1
    guessesleft= 8 - numberofguesses
    print("checking..")

    time.sleep(1)

    if (guess <number):
        print("your guess is too low! you have" + str(guessesleft) + "guesses left!")
    if (guess > number):
        print("your guess is too high! you have "+ str(guessesleft) + "guesses left!")
    if (guess == number):
        break
 except ValueError:
    print("please enter a valid number !")

else:
    if (guess < 1 or guess > 50):
        print("Please enter a number between 1-50!")
if (guess == number):
    print("congrats  you guessed number in " + str(numberofguesses) + "tries :)")
else:
    print("sorry the number i was thinking was " + str(number) + " :)")


