#emojize
import random
import emoji
user = input("Input: ")
output = emoji.emojize(user)
print("Output: ", output)

#text
import sys
from pyfiglet import Figlet
figlet = Figlet()
figlet.getFonts()

if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    isRandomFont = False
else:
    sys.exit(1)
    
saying = input("Input :")

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
        print("Output :")
        print(figlet.renderText(saying))
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())
    print("Output :")
    print(figlet.renderText(saying))