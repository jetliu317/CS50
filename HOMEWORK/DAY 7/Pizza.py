#DAY 7-2
from email import header
import sys
import csv
from tabulate import tabulate

def main():
    command()
    with open(sys.argv[1], 'r') as menu:
        table = []
        for line in menu:
            reader = csv.reader(menu)
            for row in reader:
                table.append(row)
            print(tabulate(table[2:], headers = table[0], tablefmt = 'grid' ))
    
def command():
    if len(sys.argv) < 2:
        return sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        return sys.exit("Too many command-line arguments")
    elif '.csv' not in sys.argv[1]:
        return sys.exit("Not a csv file.")
    else:
        try:
            with open(sys.argv[1]) as file:
                pass
        except FileNotFoundError:
            return sys.exit('File doesn\'t exist')
        
if __name__ == '__main__':
    main()