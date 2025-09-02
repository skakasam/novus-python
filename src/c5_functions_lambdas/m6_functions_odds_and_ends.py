"""Python Functions Odds and Ends"""


# Functions can be passed around as arguments to other functions.
def singler(x):
    """Return the single of x."""
    return 1 * x


def doubler(x):
    """Return the double of x."""
    return 2 * x


def triple(x):
    """Return the triple of x."""
    return 3 * x


multipliers = [(singler, 5), (doubler, 10), (triple, 6)]

for func, value in multipliers:
    print(f"{func.__name__}({value})={func(value)}")


# Functions can created as closures to retain state from enclosing scope
def make_multiplier(factor):
    def multiplier(x):
        return factor * x

    return multiplier


doubler = make_multiplier(2)
tripler = make_multiplier(3)

print(doubler(5))
print(tripler(5))


# Function introspection
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


print(f"{greet.__name__ = }")  # Function name
print(f"{greet.__doc__ = }")  # Function docstring
