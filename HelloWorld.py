import sys


def example1():
    print("Hello, World")


def example2():
    mystring = sys.argv[1]
    print("Hello", mystring)


# Argument required when run
def example3():
    # or code breaks right here
    try:
        mystring = sys.argv[1]
    except:
        mystring = "World"
    print("Hello", mystring)
    return


if __name__ == "__main__":
    example2()



