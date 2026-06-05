a=input("Enter a odd number: ")
a=int(a)
if a%2==1:
    pass
else:
    exit()
num=[a]
values=[10]
result=map(lambda x,y:x+y,num,values)
print("The addition of two lists is:")
print(list(result))


letter=['A.','B.','C.']
Fruits=[Apple,Banana,Cherry]
result=map(lambda x,y:x+y,letter,Fruits)
print("The addition of two lists is:")
print(list(result))