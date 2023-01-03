import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    if working := re.search(r'([0-9]*[0-9])+\:?([0-9][0-9])* (AM|PM)+ to ([0-9]*[0-9])+\:?([0-9][0-9])* (AM|PM)+', s, re.IGNORECASE):
        if int(working.group(1)) >12 or int(working.group(4)) >12 or int(working.group(2)) >59 or int(working.group(5)) >59:
            return False
        i = int(working.group(1)) + 12
        j = int(working.group(4)) + 12
        if 'PM' in working.group(3) and 'PM' in working.group(6):
            return(f'{i:02}:{working.group(2):02} to {j:02}:{working.group(5):02}')
        elif 'PM' in working.group(3) and 'AM' in working.group(6):
            return(f'{i:02}:{working.group(2):02} to {working.group(4):01}:{working.group(5):02}')
        elif 'AM' in working.group(3) and 'PM' in working.group(6):
            return(f'{working.group(1):01}:{working.group(2):02} to {j:02}:{working.group(5):02}')
    
    else:
        return 'invalid'
if __name__ == "__main__":
    main()