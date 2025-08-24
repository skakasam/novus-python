"""Python Variables Practice Module"""

from typing import Dict

################################################################################
# Variables are labels that allow us to store, modify, and retrieve data easily
# in memory. They are typically defined in snake_case (underscore between words)
# and can hold various data types such as strings, numbers, lists, dictionaries,
# custom types etc.
################################################################################
message: str = "Hello, Python!"
print(message)

################################################################################
# Constant variables are typically defined in uppercase to indicate they should
# not change. Python does not enforce immutability, but it's a convention to
# treat these as constants.
################################################################################
PI: float = 3.14159
print(PI)  # Prints 3.14159

MAX_CONNECTIONS: int = 100
print(MAX_CONNECTIONS)  # Prints 100

ORGANIZATION_INFO: Dict[str, str] = {"name": "Novus Skills", "course": "Python"}
print(ORGANIZATION_INFO)

#################################################################################
# Multiple assignment
#################################################################################
name, age, occupation = "John", 32, "Programmer"
print(name, age, occupation)  # Prints John 32 Programmer
