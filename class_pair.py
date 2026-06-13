#create a class
class pair_elements:
    def twoSum(self, nums, target):
        #create an empty dictionary
        lookup={}

        #Interate through the tuple
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], i]

#Take an input of sum from user
value=int(input("Enter the sum for which you want to find the pair:"))
print("index1=%d,index2=%d" % pair_elements().twoSum((10,20,30,40,50,60,70), value))