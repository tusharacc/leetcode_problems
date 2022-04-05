def maxArea( height):
    temp = sorted(height)
    maxHeight = temp[-1]
    index = height.index(maxHeight)
    next = -2
    maxVolume = 0
    while True:
        secondMax = temp[next]
        anotherCopy = height.copy()
        anotherCopy[index] = 0
        secondMaxIndex = anotherCopy.index(secondMax)
        volume = abs(secondMaxIndex-index)*secondMax
        if volume > maxVolume:
            maxVolume = volume
        next -= 1
        if next + len(height) == 0:
            break
        
    return maxVolume

if __name__ == '__main__':
    #print (maxArea([1,8,6,2,5,4,8,3,7]))
    #print (maxArea([1,2]))
    print (maxArea([1,2,1])) #fails for this case, sorting is not the answer