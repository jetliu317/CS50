import re

email = input('What\'s your email? ')

if re.search(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$',email):
    print('valid')
else:
    print('invalid')
