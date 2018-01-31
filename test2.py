# This is a simple python script to test python and github
# Test using the online tutorial to learn Object-Oriented Programming

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)

decorated_display()
