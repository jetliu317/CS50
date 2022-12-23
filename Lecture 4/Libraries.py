from random import choice
#import random
coin = choice(["head", "tails"])
#coin = random.choice(["heads", "tails"])
print(coin)

from random import randint
number = randint(1,100)
print(number)

from random import shuffle
cards = ["jack","queen","king"]
shuffle(cards)
for card in cards:
    print(card)
    
from statistics import median
average = median([100,30])
print(average)