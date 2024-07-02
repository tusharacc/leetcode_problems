'''
Given k linked lists where each one is sorted in the ascending order, merge all of them into a single sorted linked list.
'''
# def merge(lists: list,start,middle,end):
#     print (lists[start:middle+1])
#     print (lists[middle+1:end+1])
#     index1: int = 0
#     index2: int = 0
#     temp:list = []

#     while index1 < len(lists[start:middle+1]) and index2 < len(lists[middle+1: end + 1]) :
#         if lists[start:middle+1][index1] < lists[middle+1: end + 1][index2]:
#             temp.append(lists[start:middle+1][index1])
#             index1 += 1
#         else:
#             temp.append(lists[middle+1:end+1][index2])
#             index2 += 1
    
#     while index1 < len(lists[start:middle+1]):
#         temp.append(lists[start:middle+1][index1])
#         index1 += 1
    
#     while index2 < len(lists[middle+1: end + 1]):
#         temp.append(lists[middle+1: end + 1][index2])
#         index2 += 1


# def divide(lists: list,start: int,end: int):
#     if start == end:
#         return
#     else:
#         length: int = len(lists)
#         middle = start + (end - start) // 2
#         divide(lists, start,middle)
#         divide(lists,middle+1,end)
#         merge(lists,start,middle,end)
def merge(list1,list2):
    index1 = 0
    index2 = 0
    temp = []
    index = 0
    while index1 <= len(list1)-1 and index2 <= len(list2)-1:
        if list1[index1] < list2[index2]:
            temp.append(list1[index1])
            index1 += 1
        else:
            temp.append(list2[index2])
            index2 += 1
    
    
    while index1 <= len(list1)-1:
        temp.append(list1[index1])
        index1 += 1

    while index2 <= len(list2)-1:
        temp.append(list2[index2])
        index2 += 1

    return temp

def merge_in_place(merged_array,array):
    temp = merge(merged_array,array)
    return temp
    
def merge_k_lists(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    i = 0
    j = len(lists)-1
    merged_array = []
    while i < j:
        array = merge(lists[i],lists[j])
        merged_array = merge(merged_array,array)
        i += 1
        j -= 1
    return merged_array

  

if __name__ == '__main__':
    array = [[1,2,3],[4,5,6],[3,4],[-3,5,8]]
    print(merge_k_lists(array))