def main_1():
    cap = input("Input :")
    print("Output: ", shorten(cap))

def shorten(answer):
    item = ''
    for letter in answer:
        if not letter in ["a", "e", "i", "o","u", "A", "E", "I", "O", "U"]:
            item += letter
    return item

main_1()

def main_2():
    fraction = input("Fraction :")
    print(get_fraction(fraction))
    
def get_fraction(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            fraction = int(x) / int(y)
            if fraction == 0.75:
                return "75%"
            elif fraction == 0.50:
                return "50%"
            elif fraction == 0.25:
                return "25%"
            elif fraction >= 0.9:
                return "FULL"
            elif fraction <= 0.1:
                return"EMPTY"
        except (ValueError, ZeroDivisionError) :
            pass
        else:
            break
        
main_2()

def main_3():
    greet = input('Greet :')
    print(greeting(greet))
    
def greeting(greet):
    if greet == 'hello' or greet == 'Hello':
        return "$0"
    elif greet[0] == 'h' or greet[0] == 'H':
        return "$20"
    else:
       return "$100"
   
   main_3()