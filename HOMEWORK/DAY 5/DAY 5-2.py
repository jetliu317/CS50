#inflect
import inflect
p = inflect.engine()

name = []
while True:
    try:
        adieu = input("Name: ")
        name.append(adieu)
    except EOFError:
        print()
        break
output = p.join(name)
print("Adieu, Adieu to ", output)

#Guessing game
import random

level = int(input("Level:"))

while True:
    try:
        user_type = int(input("Guess:"))
        if user_type < random.randint(1,user_type):
            print('Too small!')
        elif user_type > random.randint(1,user_type):
            print('Too large!')
        else:
            print('Just right!')
    except ValueError:
        pass