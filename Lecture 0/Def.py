#def
def hello(to="World"):
    print("Hello, ", to)

hello()

name = input("What's your name? ").title().strip()
hello(name)

