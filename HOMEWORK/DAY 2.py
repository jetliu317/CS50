# Booleen
def main():
    x = input("What's the answer of the Universe, Life and everything? ")
    if is_42(x):
        print("Yes")
    else:
        print("No")

def is_42(n):
    return True if n == '42' or n == "forty two" or n == "forty-two" else False

# main()

# Greeting
def greet():
    x = input("Greeting : ")
    if greet_with_hello(x):
        print("$0")
    elif greet_with_h(x):
        print("$20")
    else:
        print("$100")
  
def greet_with_hello(n2):
    return True if n2 == "hello" else False

def greet_with_h(n1):
    return True if n1[0] == "H" or n1[0] == "h" else False
        
# greet()

# Extensions
def extent():
    x = input("File name : ")
    if is_gif(x):
        print("image/gif")
    elif is_jpeg(x):
        print("image/jpeg")
    else:
        print("application/octet-stream")

def is_gif(n3):
    return True if n3[-4:] == ".gif" else False

def is_jpeg(n4):
    return True if n4[-4:] == ".jpg" or n4[-5:] == ".jpeg" else False

# extent()

# Interpreter
def math():
    expression = input("Interpreter : ")
    x, y, z = expression.split(" ")
    new_x = float(x)
    new_z = float(z)
    if  y == "+" :
        print(new_x + new_z)
    elif y == "-":
        print(new_x - new_z)
    elif y == "*":
        print(new_x * new_z)
    elif y == "/":
        print(new_x % new_z) 
    
# math()

# Meal Time
def meal():
    time = input("What time is it? ")
    hours, minutes = time.split(":")
    0 <= int(minutes) <= 59
    if 7 == int(hours) or int(hours) == 8 :
        print("It's breakfast time.")
    elif 12 == int(hours) or int(hours) == 13 :
        print("It's lunch time.")
    elif 18 == int(hours) or int(hours) == 19 :
        print("It's dinner time.")
    else:
        print("It's not meal time, pig.")

meal()
        
    