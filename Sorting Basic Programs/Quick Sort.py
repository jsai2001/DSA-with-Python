'''Function that consider last element as pivot ,
Place the pivot at its exact position and place
smaller elements to left of pivot and 
greater elements to right of pivot'''

# video link to refer https://youtu.be/9KBwdDEwal8

#----------------------------------------------------
# 1) partition function is used to find the sorted position of the pivot in the array
# 2) We does the selecting the pivot to the right of the array and perform step 1 , 
# in recursive, until we are having simpler subarray's of size 1 , which will also be
# arranged in sorted order by using the quick sort algorithm
#----------------------------------------------------
def quicksort(arr,left,right):
    if left < right:
        partition_pos = partition(arr,left,right)
        quicksort(arr,left,partition_pos-1)
        quicksort(arr,partition_pos+1,right)
def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i
arr = [22,11,88,66,55,77,33,44]
quicksort(arr,0,len(arr)-1)
print(arr)
        