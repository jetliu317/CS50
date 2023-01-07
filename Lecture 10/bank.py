class Account:
    def __init__(self):
        self._balance = 0
        
    def __str__(self):
        return (f'Blance: {self.balance}')
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
        
    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    while True:
        try:
            deposit_or_withdraw = input('D/W?').capitalize()
            if deposit_or_withdraw == 'D':
                while True:
                    try:
                        account.deposit(int(input('Input amount: ')))
                        print(account)
                    except EOFError:
                        break
            if deposit_or_withdraw == 'W':
                while True:
                    try:
                        account.withdraw(int(input('Input amount: ')))
                        print(account)
                    except EOFError:
                        break
        except EOFError:
            break
if __name__ == '__main__':
    main()