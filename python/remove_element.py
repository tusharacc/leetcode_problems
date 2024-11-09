from typing import List

def removeElement( nums: List[int], val: int) -> int:
    nums[:] = [num for num in nums if num != val]
    return len(nums)

if __name__ == '__main__':
    nums = [2,3,3,2]
    print ("id of nums", id(nums))
    k = removeElement(nums,3)
    print ("id after remove Element", id(nums))
    print (k, nums)