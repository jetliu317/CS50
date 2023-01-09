import argparse

parser = argparse.ArgumentParser(description='meow like a cat')
parser.add_argument('-n', default= 1, help='number of time to meow', type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print('meow')

'''
import sys
if len(sys.argv) == 1:
    print('meow')
elif len(sys.argv) == 3:
    n = int(sys.argv[2])
    meows = 'meow\n' * n
    print (f'{meows}', end = '')
'''
    # for _ in range(n):
    #     print('meow')
'''
else:
    print('usage: meow.py')
'''