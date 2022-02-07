
from typing import List

def findMedianSortedArrays( nums1: List[int], nums2: List[int]) -> float:
    nums1 += nums2
    nums1.sort()
    length_of_list = len(nums1)
    if (length_of_list%2 == 0):
        ceil,floor = length_of_list//2,length_of_list//2 - 1
        return (nums1[ceil]+ nums1[floor])/2
    else:
        mid = (length_of_list+1)//2 - 1
        return nums1[mid]
    
    
if __name__ == '__main__':
    print(findMedianSortedArrays([1,2],[3,4]))
    #print(findMedianSortedArrays([1,3],[2]))