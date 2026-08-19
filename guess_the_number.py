import random

number=random.randint(1,100)
guess = 0

while guess!=number:
    guess = int(input("guess the number:"))
    if guess<number:
        print("too low")
    elif guess>number:
        print ("too high")


print("you won!")