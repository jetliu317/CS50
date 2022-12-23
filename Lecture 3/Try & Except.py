# Value error
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            #=return int(input("What's x? "))
            #or you can put break (return x) here
        except ValueError:
            print("x is not an interger.")
        else:
            break
    return x

main()
    

     
     