import random

Numbertoguess = random.randint(0,100)

while True:
    Guessed_Number = int(input('Please enter the guess: '))

    if Guessed_Number < Numbertoguess:
        print("Small Number")
    elif Guessed_Number > Numbertoguess:
        print("Big Number")
    else:
        print("Right")
        break