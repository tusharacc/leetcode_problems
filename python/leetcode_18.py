def fourSum(nums, target):
    nums.sort()
    result = []
    for i,v1 in enumerate(nums):
        if i == len(nums) - 4:
            break
        j = i+1

        while True:
            if j == len(nums) - 5:
                break
            if v1 == nums[j]:
                j += 1
                continue     
            else:
                k = j+1
                
                l = len(nums)-1
                #if l == k:
                while True:
                    if nums[k] == nums[j]:
                        k += 1
                        continue
                    else:
                        print (f"i: {i}, j: {j}, k: {k}, l: {l}")
                        if nums[i]+nums[j]+nums[k]+nums[l] == target:
                            result.append([nums[i],nums[j],nums[k],nums[l]])
                        l -= 1
                        if l == k:
                            break
            j += 1




if __name__ == '__main__':
    print (fourSum([1,0,-1,0,-2,2],3))