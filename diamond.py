#take input from user
rowSize=int(input("Enter the number of rows:"))
if rowSize%2==0:#conditions
    halfDiamond=int(rowSize/2)
else:
    halfDiamond=int(rowSize/2)
space=halfDiamond-1
#loop for upper part
for i in range(1,halfDiamond+1):
    for j in range(1,space+1):
        print(end="")
    space=space=1
    num=1
    for j in range(2*i-1):
      print(end=str(num))#Display result
    #increasing number in each column
    num=num+1
print()