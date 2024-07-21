
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
        if d.get(item,None) == None:
            d[item] = 1
        else:
            d[item] += 1

    key_values_tuple = sorted(d.items(),key=lambda x: x[1],reverse=True)
    return [x[0] for x in key_values_tuple[0:k]]

if __name__ == '__main__':
    arr = [1, 2, 3, 2, 4, 3, 1]
    print (find_top_k_frequent_elements(arr,2))