def add (P,Q):
#This function adds two numbers and returns the result
    return P+Q
def substract (P,Q):
#This function subtracts two numbers and returns the result
    return P-Q
def multiply (P,Q):
#This function multiplies two numbers and returns the result
    return P*Q
def divide (P,Q):
#This function divides two numbers and returns the result
    return P/Q
#now we will take input from the user
print("Please select the operation.")
print("A.Add")
print("B.Subtract")
print("C.Multiply")
print("D.Divide")

choice=input("Enter choice (A/B/C/D): ")

num_1=int(input("Enter first number:"))
num_2=int(input("Enter second number:"))
if choice=="A":
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice=="B":
    print(num_1,"-",num_2,"=",substract(num_1,num_2))
elif choice=="C":
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif choice=="D":
    print(num_1,"/",num_2,"=",divide(num_1,num_2))
else:
    print("Invalid input")