# This is a simple python script to test python and github
# Test using the online tutorial to learn Object-Oriented Programming

# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function
#
# def display():
#     print('display function ran')
#
# decorated_display = decorator_function(display)
#
# decorated_display()

noprimes = [ j for i in range(2,9) for j in range(i*2, 50, i) ]
primes = [x for x in range(2,50) if x not in noprimes]
print(noprimes)
print(primes)
