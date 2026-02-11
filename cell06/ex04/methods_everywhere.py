import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    while len(s) < 8:
        s += 'Z'
    print(s)

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for word in args:
        if len(word) > 8:
            shrink(word)
        elif len(word) < 8:
            enlarge(word)
        else:
            print(word)
