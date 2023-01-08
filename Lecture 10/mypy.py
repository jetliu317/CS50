def meow(n:int) -> str:
    return 'meow\n' * n 

numbers: int = int(input('Times :'))
meows = meow(numbers)

print(meows, end ='')