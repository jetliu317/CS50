# Little Professor
import random

def main():
    level = get_level()
    print(x, '+', y, '=', end='')
    ans = int(input())
    print(ans)
    while True:
        if ans == x+y:
            break
        else:
            print('eee')

def get_level():
    while True:
        try:
            level = int(input('Level:'))
            if 1 <= level <=3:
                break
        except:
            pass 
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y
 
            

if __name__ == "__main__":
    main()