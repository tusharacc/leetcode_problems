from typing import List


def twoSum( nums: List[int], target: int) -> List[int]:
    # end = (len(nums)//2)+1
    # print (end)
    # for k,item in enumerate(nums[:end]):
    #     next = target - item
    #     count = 1 if next == item else 0
    #     if nums.count(next) > count:
    #         return [k,nums.index(next,k+1)]
    
    for i in range(len(nums)):
       potential = target - nums[i]
       print (nums.index(potential))
       if potential in nums and nums.index(potential) != i:
           return[i, nums.index(potential)]
    # sorted_array = sorted(nums)
    # print (sorted_array)
    # length = len(nums)
    # for k,v in enumerate(sorted_array):
    #     print (k,v)
    #     j = k + 1
    #     while j <= length - 1:
    #         if v + sorted_array[j] == target:
    #             first = nums.index(v)
    #             return [first,nums.index(sorted_array[j],first+1)]
    #         elif v + sorted_array[j] > target:
    #             continue
    #         j += 1


    # for i in range(0,len(nums)-1):
    #     #print ("Number",nums[i])
    #     for j in range(i+1,len(nums)):
    #         #print ("item", item)
    #         if nums[i]+nums[j] == target:
    #             return [i,j]

if __name__ == '__main__':
    print(twoSum([3,3],6))