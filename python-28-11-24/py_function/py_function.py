def arbitrary_positional_arguments(*args):
    print(args, type(args))
    for arg in args:
        print(arg)

arbitrary_positional_arguments(2,3,4,6,7,"H")

def find_factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return (x * find_factorial(x-1))
    
num =1000
print("The factorial of", num, "is", find_factorial(num))