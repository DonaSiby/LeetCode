class Solution1:
    #Here the time and space complexity is O(n)
    def twoSum(self, num: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(num)):
            complement = target-num[i]
            if complement in hashmap:
                return[i, hashmap[complement]]
            hashmap[num[i]] = i
         
    #Here the time complexity is O(n) and space complexity is O(1)
    def twoSumSort(self,num: list[int],target: int)-> list[int]:
        left=0
        right=len(num)-1
        while left<right:
            sum=num[left]+num[right]
            if sum == target:
                return[left,right]
            elif sum>target:
                right=right-1
            else:
                left=left+1
       
  
s=Solution1()
num=[2,1,5,3]
num1=[1,2,3,5]
target=4
print(s.twoSum(num, target))
print(s.twoSumSort(num1,target))

