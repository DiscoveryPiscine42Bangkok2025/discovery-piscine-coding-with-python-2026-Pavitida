import sys

if len(sys.argv) == 1:
    print("none")
else:
    printed = False

    for word in sys.argv[1:]:
        if not word.endswith("ism"):
            print(word + "ism")
            printed = True

    if not printed:
        print("none")
