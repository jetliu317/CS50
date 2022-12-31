#DAY 7-3
import sys
import csv

def main():
    command()
    after = []
    with open(sys.argv[1], 'r') as before:
        reader = csv.DictReader(before)
        for row in reader:
            split_name = row['name'].split(',')
            after.append({f'first': split_name[1].lstrip(), 'last': split_name[0].lstrip(), 'house': row['house']})
    with open(sys.argv[2], 'w+') as after_h:
        writer = csv.DictWriter(after_h, fieldnames = ['first','last','house'])
        writer.writerow({'first':'first','last':'last','house':'house'})
        for row in after:
            writer.writerow({'first':row['first'],'last':row['last'],'house':row['house']})
            
def command():
    if len(sys.argv) < 3:
        return sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        return sys.exit("Too many command-line arguments")
    elif '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:
        return sys.exit("Not a csv file.")
    else:
        try:
            with open(sys.argv[1]) as file:
                pass
        except FileNotFoundError:
            return sys.exit('File doesn\'t exist')
        
if __name__ == '__main__':
    main()