'''
Given an array and a target number, find the indices of the two values from the array that sum up to the given target number.
'''

def two_sum(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    numbers_sorted = sorted(numbers)


        
    return [-1,-1]

if __name__ == '__main__':
    array: list = [4, 1, 5, 0, -1]
    # array: list =  [5, 5, 5, 5, 5, 5], target = 10
    # array: list = [5, 3, 10, 45, 1], target = 6
    print (two_sum(array,10))
