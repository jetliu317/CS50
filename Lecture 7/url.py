import re

url = input('URL: ').strip()

if matches := re.search(r'^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)', url, re.IGNORECASE):
    print(f'username: ', matches.group(1))
else:
    print('not a twitter url or invalid username')