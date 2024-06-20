'''
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.
'''

def count(arr,start,middle,end,counter):
    pass

def initiate(arr,start,end,counter):
    if (start==end):
        return
    middle = start + (end-start)/2
    initiate(arr,start,middle)
    initiate(arr,middle+1,end)
    count(arr,start,middle,end,counter)

# arr[]: Input Array
# N : Size of the Array arr[]
#Function to count inversions in the array.
def inversionCount(self, n, arr):
    start = 0
    end = n
    counter = 0
    initiate(arr,start,end,counter)