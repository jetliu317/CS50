import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("tToo much arguments")
#else:
#    print("Hello, my name is", sys.argv)
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)

