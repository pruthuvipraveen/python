import random

num = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == num:
        print("Congratulations! !")
        break
    else:
        print("The number is wrong. Try again.")