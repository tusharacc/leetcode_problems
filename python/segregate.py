def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """

    """
    Solution 1
    start = 0
    end = len(numbers)-1
    while start < end:
        if numbers[start]%2 == 0:
            start += 1
        else:
            if numbers[end]%2 == 0:
                numbers[start], numbers[end] = numbers[end], numbers[start]
                start += 1
            end -= 1
        
    return numbers
    
    """

    """
    Solution 2
    """
    odd = []
    index = 0
    while True:
        if numbers[index]%2 == 1:
            odd.append(numbers.pop(index))
        else:
            index+= 1
        if index >= len(numbers):
            break
    return numbers + odd
    
if __name__ == '__main__':
    array = [4, 9, 5, 2, 9, 5, 7, 10]
    print(segregate_evens_and_odds(array))