import sys


def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "Guest"
    print(greet(name))
