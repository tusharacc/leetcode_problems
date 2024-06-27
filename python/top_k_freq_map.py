
'''
Given an integer array and a number k, find the k most frequent elements in the array.

Example One

{
"arr": [1, 2, 3, 2, 4, 3, 1],
"k": 2
}
Output:

[3, 1]
'''
def find_top_k_frequent_elements(arr, k):
    d = {}
    for item in arr:
        if d.get(item,None)