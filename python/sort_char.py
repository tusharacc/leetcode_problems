'''
Given a list of characters, sort it in the non-decreasing order based on ASCII values of characters.
'''

def merge(arr,start,middle,end):
    temp_arr = []
    index = middle + 1
    temp_start = start
    while start <= middle and index <= end:
        if arr[start] < arr[index]:
            temp_arr.append(arr[start])
            start += 1
        else:
            temp_arr.append(arr[index])
            index += 1
            
    while start <= middle:
        temp_arr.append(arr[start])
        start += 1
        
    while index <= end:
        temp_arr.append(arr[index])
        index += 1
        
    for i in range(len(temp_arr)):
        arr[temp_start+i] = temp_arr[i]

def initiate(arr,start,end):
    if start == end:
        return
    middle = start + (end-start)//2
    initiate(arr,start,middle)
    initiate(arr,middle+1, end)
    merge(arr,start,middle,end)

def merge_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    start = 0
    end = len(arr)-1
    initiate(arr,start,end)
    return arr

def sort_array(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    ascii_value: list = [ord(x) for x in arr]
    ascii_value = merge_sort(ascii_value)
    for k,v in enumerate(ascii_value):
        arr[k] = chr(v)

    return arr

if __name__ == '__main__':
    arr: list = ["a", "s", "d", "f", "g", "*", "&", "!", "z", "y"]
    print (sort_array(arr))