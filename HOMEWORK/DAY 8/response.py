import re
from email_validator import validate_email, EmailNotValidError
import validators

def main():
    mail = input('What\'s your email address? ')
    if validate(mail):
        print('Valid')
    else:
        print('Invalid')
    
def validate(mail):
    try:
        if validators.email(mail):
            return 'Valid'
    except EmailNotValidError:
        return 'Invalid'
if __name__ == '__main__':
    main()
    
