import math, random

def partition(arr):
    start = 1
    end = len(arr)-1
    while start < end:
        if arr[start] < arr[0]:
            start += 1
        else:
            arr[end],arr[start] = arr[start], arr[end]
            end -= 1

    arr[0],arr[end] = arr[end],arr[0]

    return end

def get_neighbours(arr,k):
    pivot_index = random.randrange(0,len(arr)-1)

    arr[0],arr[pivot_index] = arr[pivot_index],arr[0]
    pivot_index = partition(arr)
    if pivot_index == k:
        return arr[0:k+1]
    elif pivot_index > k:
        get_neighbours(arr[k:],)
        


def nearest_neighbours(p_x, p_y, k, n_points):
    distance_map = {}
    distance_array = []
    for point in n_points:
        d = round(math.sqrt(pow(p_x - point[0],2)+ pow(p_y - point[1],2)),2)
        distance_map[d] = point
        distance_array.append(d)

        least_distance = 
    
