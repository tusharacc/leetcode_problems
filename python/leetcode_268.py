'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

from typing import List


def missingNumber(nums: List[int]) -> int:
    size: int = len(nums)
    var: int = 0
    for item in nums:
       var |= (1 << item)

    for k,v in enumerate(bin(var)[2:][::-1]):
        if v == '0':
            return k
        
    
if __name__ == '__main__':
    nums: List[int] = [0,1,3]
    print (missingNumber(nums))
