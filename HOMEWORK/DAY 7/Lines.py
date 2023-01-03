#DAY 7-2
from curses.ascii import isalpha, isspace
from fileinput import close
import sys

def main():
    command()
    lines = 0
    with open(sys.argv[1],'r') as count_line:
        for line in count_line.readlines():
            if '#' in line[0]:
                lines += 0
            elif line.isspace():
                lines += 0
            else:
                lines += 1
    print(lines)
    close()

def command():
    if len(sys.argv) < 2:
        return sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        return sys.exit("Too many command-line arguments")
    elif '.py' not in sys.argv[1]:
        return sys.exit("Not a python file.")
    else:
        try:
            with open(sys.argv[1]) as file:
                pass
        except FileNotFoundError:
            return sys.exit('File doesn\'t exist')
        
if __name__ == '__main__':
    main()
        
