#take input
rows=int(input("Enter the number of rows:"))
number=1#intialize number
print("Floy's triangle:")
#outer loop to handle number of rows
for i in range(0,rows):
    #inner loop to handle number of columns
    for j in range(0,i+1):
        print(number,end="")
        number=number+1
    print()