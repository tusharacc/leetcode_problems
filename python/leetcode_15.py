from typing import List

@profile
def threeSum( nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    result = []
    sum_abs = {}
    length_of_list = len(nums)
    for i in range(0,length_of_list-2):
        j = i + 1
        k = length_of_list - 1
        if i > 0 and nums[i] == nums[i - 1]:
                continue
        while j < k:
            
            sum = nums[i]+nums[j]+nums[k]
            if sum == 0:
                result.append([nums[i],nums[j],nums[k]])
                k -= 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            elif sum > 0:
                k -= 1
            else:
                j += 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1

      
    return result

if __name__ == '__main__':
    test_array = [[0,0],[-2,0,1,1,2],[-1,0,1,2,-1,-4],list(range(-20,21))]
    test_array = [[-1,0,1,2,-1,-4,-2,-3,3,0,4]]
    for item in test_array:
        print(threeSum(item))