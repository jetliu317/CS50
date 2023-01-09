

def meow(n:int) -> str:
    """
    eat my shit
    """
    return 'meow\n' * n 


numbers: int = int(input('Times :'))
meows = meow(numbers)

print(meows, end ='')
print(meow.__doc__) 

