import sys


def greet(name):
    normalized_name = name.strip()
    if not normalized_name:
        normalized_name = "Guest"
    return f"Hello, {normalized_name}!"


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "Guest"
    print(greet(name))
