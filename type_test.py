__author__ = 'Harry Ingles'

# Check if the entered digit can be converted to an integer


def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

# Check if the entered value can be converted to a string


def is_str(n):
    try:
        str(n)
        return True
    except ValueError:
        return False

# Check if the entered value can be converted to a float


def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def is_file(file_name):  # Function used to check if the input is a file name in the current folder
    try:
        file = open(file_name, 'r')
        file.read()
        return True
    except:
        return False
