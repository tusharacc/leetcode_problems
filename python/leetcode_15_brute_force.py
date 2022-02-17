from typing import List

@profile
def threeSum( nums: List[int]) -> List[List[int]]:
    result = []
    sum_abs = {}
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k] == 0:
                    if sum_abs.get(abs(nums[i])+abs(nums[j])+abs(nums[k]),None) == None:
                        result.append([nums[i],nums[j],nums[k]])
                        sum_abs[ abs(nums[i]) + abs(nums[j]) + abs(nums[k])] = [[nums[i],nums[j],nums[k]]]
                    else:
                        found = False
                        for item in sum_abs[ abs(nums[i]) + abs(nums[j]) + abs(nums[k])]:
                            if nums[i] in item and nums[j] in item and nums[k] in item:
                                found = True
                                break
                        if not found:
                            result.append([nums[i],nums[j],nums[k]])
                            sum_abs[ abs(nums[i]) + abs(nums[j]) + abs(nums[k])].append([nums[i],nums[j],nums[k]])
    return result

if __name__ == '__main__':
    test_array = [[0,0],[-2,0,1,1,2],[-1,0,1,2,-1,-4],list(range(-20,21))]

    for item in test_array:
        print(threeSum(item))