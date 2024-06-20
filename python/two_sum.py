'''
Given an array sorted in non-decreasing order and a target number, find the indices of the two values from the array that sum up to the given target number.
'''

def pair_sum_sorted_array(numbers, target):
    start: int = 0
    end: int = len(numbers) - 1
    answer: list = []
    while True:
        if numbers[start] + numbers[end] == target:
            answer = answer + [start,end]
            break
        elif numbers[start] + numbers[end] < target:
            start += 1
        elif numbers[start] + numbers[end] > target:
            end -= 1

        if start >= end:
            break
    return  answer if answer else [-1,-1]

if __name__ == '__main__':
    array: list = [1, 2, 3, 5, 10]
    print (pair_sum_sorted_array(array,7))