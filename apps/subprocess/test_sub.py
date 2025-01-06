import sys


def main():
    print("print to stdin")
    print("print to stderr", file=sys.stdout)


if __name__ == "__main__":
    main()
