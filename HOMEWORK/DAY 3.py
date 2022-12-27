# CamelCase
letters = input("camelCase :")
print("snake_case:", end = "")

for letter in letters:
    if letter.isupper():
        print("_" + letter.lower(), end = "")
    else:
        print(letter)
        
# Coke Machine
amount_due = 50

while amount_due > 0:
    print("Amount due :", amount_due)
    coin = int(input("Insert coin :"))
    if coin in [5, 10, 25]:
        amount_due -= coin
change_owed = abs(amount_due)
print("Change owed :", change_owed)

#twwttr
def main_2():
    cap = input("Input :")
    print("Output: ", shorten(cap))

def shorten(answer):
    for letter in answer:
        item = ''
        if not letter in ["a", "e", "i", "o","u", "A", "E", "I", "O", "U"]:
            item += letter
    return item

main_2()
        
# vanity plate
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    i = 0
    while 0 > len(s):
        if s[i].isalpha() == False: 
            if s[i] == "0":
                return False
        i += 1
    for word in s:
        if word in [".", " ", "!", "?"]:
            return False
    return True
main()
    
# Nutrition

Cal = {"apple" : 130,
       "avocado" : 50,
       "banana" : 110,
       "cantaloupe" : 50,
       "grapefruit" : 60,
       "grapes" : 90,
       "honeydew melom" : 50,
       "kiwifruit" : 90,
       "lemon" : 15,
       "lime" : 20,
       "nectarine" : 60,
       "orange" : 80,
       "peach" : 60,
       "pear" : 100,
       "pineapple" : 50,
       "plums" : 70,
       "strawberries" : 50,
       "sweet cherries" : 100,
       "tangerine" : 50,
       "watermelon" : 80
       }

asked = input("Item :")

for fruit in Cal:
    if fruit == asked:
        print("Calories :", Cal[fruit])
        

