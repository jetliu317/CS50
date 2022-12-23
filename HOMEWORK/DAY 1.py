#lowercase all the letters

# to_lower_case
def to_lower_case() : 
    lowercase = input("What do you want to say? ").lower()
    print(lowercase)
    
to_lower_case()

# #Playback speed
def slow_down():
    print("Please slow down.")
    print("Okay,", "I", "admit", "that", "I", "speak", "too", "fast", sep="...")

# #face emoji
def hello(to = ":)"):
    print("Hello", to)
hello()
hello("🙂")

def goodbye(too=":("):
    print("goodbye", too)
goodbye()
goodbye("🙁")

# E=mc^2
M = int(input("M="))
C = 300000000 * 300000000
print("E=", M * C)

#tips calculator
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(amt):
    return float(amt[1:])
        
def percent_to_float(amt):
    return float(amt[:2])/100
    
main()

