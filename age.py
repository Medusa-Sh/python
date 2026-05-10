age=input("Enter your age: ")
if not age.isdigit():
    print("Please enter a valid age.")
else:
    age = int(age)
    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")