# from typing import List
# class Solution:
#     def twosum(self, nums: List[int], target: int) -> List[int]:

a = [2,7,11,15] 
target = 9
b = 0 
# for i in a:
#     b = b + i 
#     if b == target:
#        print () 

for i,v in enumerate(a):
    index1 = i 
    index2 = i + 1 
    b = b + v
    print(index1,index2)
    if b == target:
        print(index1,index2)
    else:
        pass