from typing import List

def merge( nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for (k,v) in enumerate(nums2):
        nums1[m+k] = v
    
    nums1.sort()
        
        

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)