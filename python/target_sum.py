
def recursive(arr,k):
    if len(arr) == 1:
        if k == arr[0]:
            return True
        else:
            return False
    var = arr[0]
    if var == k:
        return True
    else:
        return recursive(arr[1:],k-var)


def check_if_sum_possible(arr, k):
    """
    Args:
     arr(list_int64)
     k(int64)
    Returns:
     bool
    """
    # Write your code here.
    if arr:
        sorted_arr = sorted(arr)
        for item in sorted_arr:
            if item == k:
                return True
        for i in range(len(sorted_arr)):
            value = recursive(sorted_arr[i:],k)
            if value:
                return True
        # sorted_arr = sorted(arr)
        # i = 0
        # j = len(arr)-1
        # sum_arr = sum(sorted_arr)
        # if sum_arr == k:
        #     return True
        # elif sum_arr < k:
        #     if k == arr[0]:
        #         return True
        #     else:
        #         return check_if_sum_possible(arr[1:],k)
        # elif sum_arr > k:
        #     if k == arr[-1]:
        #         return True
        #     else:
        #         return check_if_sum_possible(arr[:-1],k)


    return False

if __name__ == '__main__':
    arr = [2,4,8]
    assert check_if_sum_possible(arr,6) == True

    arr = [2,4,8]
    assert check_if_sum_possible(arr,8) == True

    arr = [2,4,6]
    assert check_if_sum_possible(arr,5) == False

    arr = []
    assert check_if_sum_possible(arr,10) == False

    arr = [5]
    assert check_if_sum_possible(arr,5) == True

    arr = [-3,-3,-3,-3]
    assert check_if_sum_possible(arr,-12) ==True

    arr = [-3,-2,1]
    assert check_if_sum_possible(arr,-4) ==True

    arr = [-5, 8, 2, 11, -8]
    assert check_if_sum_possible(arr,14) ==True
