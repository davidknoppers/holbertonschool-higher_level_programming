#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    print("{:d} argument{:s}{:s}".format(args, "s" if args > 1 else "", "."
                                         if args <= 1 else ":"))
    for index, arg in enumerate(sys.argv[1:]):
        print("{:d}: {:s}".format(index + 1, arg))
