# Functions

# arbitrary arguments, *args
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")
greet("Alice", "Bob", "Charlie")