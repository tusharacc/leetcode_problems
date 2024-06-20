def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.

    """
    Solution 1

    temp_arr = []
    length = len(first)-1
    index_1 = 0
    index_2 = 0
    while index_1 < len(first) and index_2 < len(first):
        if first[index_1] < second[index_2]:
            temp_arr.append(first[index_1])
            index_1 += 1
        else:
            temp_arr.append(second[index_2])
            index_2 += 1
    
    while index_1 < len(first):
        temp_arr.append(first[index_1])
        index_1 += 1
    
    while index_2 < len(first):
        temp_arr.append(second[index_2])
        index_2 += 1
    
    for k,v in enumerate(temp_arr):
        second[k] = v
    return second

    """

    length = len(first)
    
    for i in range(length):
        second[length+i] = second[i]
        
    index_1 = 0
    index_2 = length
    index_3 = 0
    while index_1 < length and index_2 < 2*length:
        if first[index_1] < second[index_2]:
            second[index_3] = first[index_1]
            index_1 += 1
        else:
            second[index_3] = second[index_2]
            index_2 += 1
        index_3 += 1
    
    if index_1 < length:
        second[index_3] = first[index_1]
        index_3 += 1
        index_1 += 1
    
    if index_2 < 2*length:
        second[index_3] = second[index_2]
        index_3 += 1
        index_2 += 1
    return second

if __name__ == '__main__':
    first = [13, 21]
    second = [13,13,0,0]
    print(merge_one_into_another(first,second))

