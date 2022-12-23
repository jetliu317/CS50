#pass
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            #=return int(input("What's x? "))
            #or you can put break (return x) here
        except ValueError:
            #print("x is not a interger")
            pass
        else:
            break
    return x

main()
    