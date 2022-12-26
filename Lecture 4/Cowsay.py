import cowsay
import sys

if len(sys.argv) == 2:
    say = cowsay.trex(sys.argv[1])
    print(say)
