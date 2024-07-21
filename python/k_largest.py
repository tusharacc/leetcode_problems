'''
Given an initial list along with another list of numbers to 
be appended with the initial list and an integer k, return an array consisting of the k-th
largest element after adding each element from the first list to the second list.

Corner Cases
1. Either or both empty

Runtime

Space

Constraints:

1 <= length of both lists <= 10^5
1 <= k <= length of initial list + 1
0 <= any value in the list <= 10^9
'''

import random

def partition(arr,k):
    low = 0
    high = len(arr) - 1
    left = low + 1
    right = high
    while True:
        while left <= right and arr[left] <= arr[low]:
            left += 1
        while left <= right and arr[right] >= arr[low]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
        
    arr[low], arr[right] = arr[right], arr[low]
    return right


def find(list,k):
    if len(list) == 1:
        return list[0]
    
    pivot_index = random.randint(1,len(list)-1)
    list[0], list[pivot_index] = list[pivot_index], list[0]
    pivot_pos = partition(list,k)

    if pivot_pos == k:
        return list[k]
    elif pivot_pos > k:
        find(list[:pivot_pos],k)
    else:
        find(list[pivot_index+1:], k - pivot_index)



def kth_largest(k, initial_stream, append_stream):
    k_largest = []
    for item in initial_stream:
        append_stream.append(item)
        k_largest.append(find(append_stream,k-1))
    return k_largest

if __name__ == '__main__':
    k =  2
    initial_stream = [4, 6]
    append_stream =  [5, 2, 20]

    print (kth_largest(k,initial_stream,append_stream))

