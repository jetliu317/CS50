import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif sys.argv[2][-1:-2] != 'py':
    sys.exit("Not a python file.")