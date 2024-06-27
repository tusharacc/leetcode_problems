'''
Moore's voting algorithm

Given an array of size N, find the majority element. The majority element is the element that appears more than floor(N/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.
'''

def majority(array):
    cnt = 1
    element = array[0]
    for i in range(1,len(array)):
        if array[i] == element:
            cnt += 1
        else:
            cnt -= 0

        if cnt == 0:
            element = array[i]
            cnt = 1

    return element

if __name__ == '__main__':
    array = [1,2,3,1,4,5,6,7,8,9,1,10,11,1,13,14,1,15,]
    print (majority(array=array))
