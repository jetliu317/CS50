balance = 0

def main():
    global balance
    print('Balance: ',balance)
    deposit_or_withdraw()
    
  
    
def deposit_or_withdraw():
    global balance
    while True:
        try:
            save_minus = int(input('Input the amount that you want to deposit or withdraw: '))
            balance += save_minus
            print('Balance: ',balance)
        except (EOFError, ValueError):
            break
    
if __name__ == '__main__':
    main()