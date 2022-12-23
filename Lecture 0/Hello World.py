# Ask user for their name and age(you can put .str in the same line)
name = input("What's ypur name? ").strip().capitalize().title()
age = input("How old are you? ")

#Combine above function together
name = name.strip().capitalize().title()

#Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to the user
print("Hello,",  first)
print("Your're", age, "years old, right?")
print("Yes")

# STR end="\n"(the end of the line) & sep=' '(the string that uses to seperate two strings into a string)
print("How many family members in your family? ", end = "")
print("I got four in my family.")
print("There are six members in my family", "it's always crowded when all the family members are home", sep=", ")

# \
print("Sorry I have to go, I've got another meeting")
print("What kind of \"meeting\"? ")

#f = file
print(f"It's a kind of meeting for {age} year-old adult, haha")

