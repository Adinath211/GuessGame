import random
number=random.randint(1,9)
chances=1
print(number)
print("Number Guessing Game")
print("Guess a number between 1 and 9")
guess=int(input("Enter your guess:-"))
while chances<5:
    if guess==number:
        print("Congratulation YOU WON!!") 
        break
    else:
        print("Enter a number lower or higher than",guess)
        guess=int(input("Enter your guess:-"))
        chances=chances+1
if not chances<5:
    print("YOU LOSE!! The number is",number)