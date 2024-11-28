def arbitrary_positional_arguments(*args):
    print(args, type(args))
    for arg in args:
        print(arg)

        
arbitrary_positional_arguments(2,3,4,6,7,"H")