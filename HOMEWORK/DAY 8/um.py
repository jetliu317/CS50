import re
import sys


def main():
    print(count(input("Text: ").lower()))


def count(s):
    count_um = 0
    find = re.findall(r'\bum\b', s, re.IGNORECASE)
    if find:
        for um in find : 
            count_um += (find.count('um')) 
            return(count_um)
    else:
        return(count_um)

if __name__ == "__main__":
    main()