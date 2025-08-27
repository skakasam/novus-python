"""Python Packages Practice"""

################################################################################
# Python Regular Packages
################################################################################
# A package is a way of organizing related modules into a single directory
# hierarchy. Packages allow you to structure your code in a modular way and
# avoid naming conflicts between modules.
#
# To create a package, you need to create a directory with an __init__.py file
# inside it. The __init__.py file can be empty or can contain initialization
# code for the package.
#
# Once you have a package, you can import its modules using the dot notation.
# For example, if you have a package named 'my_package' with a module named
# 'my_module', you can import it like this:
# from my_package import my_module
################################################################################

from p1_regular_package import m1_modules_in_python as regular_module

print()
print("Importing Modules from Regular Package:")
print(f"  regular_module.__name__   : {regular_module.__name__}")
print(f"  regular_module.__file__   : {regular_module.__file__}")
print(f"  regular_module.__package__: {regular_module.__package__}")
print(" ", regular_module.greet_user(name="Alice", lang_code="es"))
print(" ", regular_module.greet_user(name="Bob", lang_code="fr"))

from p1_regular_package import greet_user

print()
print("Importing from Package:")
print(" ", greet_user(name="Alice", lang_code="es"))
print(" ", greet_user(name="Bob", lang_code="fr"))

################################################################################
# Python Namespace Packages
################################################################################
# A namespace package is a type of package that allows you to split a single
# package across multiple directories. This is useful for large packages that
# need to be developed and maintained by multiple teams.
#
# To create a namespace package, you need to create a directory without an
# __init__.py file. This allows Python to treat the directory as a namespace
# package.
#
# Once you have a namespace package, you can import its modules using the dot
# notation, just like with regular packages.
################################################################################

################################################################################
# Setting up Namespace Packages
################################################################################
# Imagine a situation where two different teams are developing modules for
# Novus-Corp, one focusing on date utilities and the other on magic numbers.
#
# Project Structure (Showing Relative Locations):
#   p2-novus-corp/
#   │
#   ├── p2a-novus-corp-dateutil/
#   │   ├── novus_corp/
#   │   │   └── date_utilities.py
#   │   └── pyproject.toml
#   │
#   ├── p2b-novus-corp-magic-numbers/
#   │   ├── novus_corp/
#   │   │   └── magic_numbers.py
#   │   └── pyproject.toml
#   │
#   └── p2c-novus-service/
#       └── novus_service.py
#
# With this we have the basic file structure of three packages. Both the utility packages,
# p2a-novus-corp-dateutil and p2b-novus-corp-magic-numbers, start by defining an implicit
# namespace package called novus_corp.
# It’s an implicit namespace package because of the absence of an __init__.py file.
#
# As for the import name, you’ll import the novus-corp-dateutil package as
# novus_corp.date_utilities and novus_corp.magic_numbers.
# In the corresponding pyproject.toml file, you fill out some information that setuptools
# needs to properly install the package.
################################################################################

################################################################################
# Installing and Using Namespace Packages
################################################################################
# To install the namespace packages, you would typically use a tool like
# setuptools. The pyproject.toml file in each package directory contains
# the necessary configuration for setuptools to recognize the package.
#
# Steps:
#   1. cd p2-novus-corp
#   2. python -m pip install -e p2a-novus-corp-dateutil
#   3. python -m pip install -e p2b-novus-corp-magic-numbers
#
# Note:
# The -e flag allows you to install the package in "editable" mode, which means
# that changes to the source code will be immediately reflected in the installed
# package without needing a reinstall. Typically, you would use this mode during
# development to test changes without constantly reinstalling the package.
# Otherwise, you would install the package normally (without -e) for production use.
#
# Note how you’re able to import both the utilities from the novus_corp namespace,
# as if both belonged to the same package.
################################################################################


from novus_corp import date_utilities, magic_numbers  # pyright: ignore[reportMissingImports]

print()
print("Importing Modules from Namespace Package:")
print(f"  Magic Number: {magic_numbers.secret_number_generator()}")
print(f"  Days to Novus Day: {date_utilities.days_to_novus_day()}")
