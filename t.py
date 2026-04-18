def functional(x):
    "This is a recursive function to find the functional of an integer"
    if x==0:
        return 1
    else:
        #calling funtion inside a function
        return x*functional(x-1)

#display result
print(functional.__doc__)
print("The factorial of 0 is", functional(0))
print("The factorial of 1 is", functional(1))
print("The factorial of 2 is", functional(2))
print("The factorial of 5 is", functional(5))
print("The factorial of 10 is", functional(10))