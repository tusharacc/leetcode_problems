from typing import List

@profile
def threeSum( nums: List[int]) -> List[List[int]]:
    result = []
    sum_abs = {}
    length_of_list = len(nums)
    for i in range(0,length_of_list-1):
        j = i + 1
        k = length_of_list - 1
        while j < length_of_list and j != k:
            #print ("index i",i,"index j",j,"index k",k)
            abs_i,abs_j,abs_k = abs(nums[i]),abs(nums[j]),abs(nums[k])
            if nums[i]+nums[j]+nums[k] == 0:
                if sum_abs.get(abs_i+abs_j+abs_k,None) == None:
                    result.append([nums[i],nums[j],nums[k]])
                    sum_abs[ abs_i+abs_j+abs_k] = [[nums[i],nums[j],nums[k]]]
                else:
                    found = False
                    for item in sum_abs[ abs_i+abs_j+abs_k]:
                        if nums[i] in item and nums[j] in item and nums[k] in item:
                            found = True
                            break
                    if not found:
                        result.append([nums[i],nums[j],nums[k]])
                        sum_abs[ abs_i+abs_j+abs_k].append([nums[i],nums[j],nums[k]])
            k -= 1
            if k == j:
                j += 1
                k = len(nums) - 1
      
    return result

if __name__ == '__main__':
    test_array = [[0,0],[-2,0,1,1,2],[-1,0,1,2,-1,-4],list(range(-20,21))]

    for item in test_array:
        print(threeSum(item))