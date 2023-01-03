import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if youtube := re.search(r'(?:https?://)?(?:www\.)?youtube\.com/embed/([a-z0-9_]+)', s, re.IGNORECASE):
        return f'https://youtu.be/{youtube.group(1)}'
    else:
        return 'invalid'

if __name__ == "__main__":
    main()