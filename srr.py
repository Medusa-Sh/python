import array as arr

#create an array
array_num=arr.array('i',[1,2,3,4,5])
print("The original array is:",array_num)

#count the number of occurrences
print("The number of occurrences of 3 is:",array_num.count(3))

#Reverse the array
array_num.reverse()
print("Reverse the order of the array:")
print(str(array_num))