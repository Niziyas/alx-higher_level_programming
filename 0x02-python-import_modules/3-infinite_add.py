#!/usr/bin/python3
if __name__ == "__main__":
    """print infinit add"""
    import sys

    total = 0
    for i in rane(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
