# Create Bubble Sort function
# Sorting from end to start of the array
def bubble_sort(arr):
    # Outer loop is for traversing the entire list n-1 times
    # So inner loop can perform the swapping and sorting operations n-1 times
    for i in range(0,len(arr)-1):
        # Every loop of the inner for loop , sorts an element to it's position
        # Basically the sorting happens from the last
        # Each iteration , one element will be sorted from the right
        for j in range(len(arr)-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr = [5,3,8,6,7,2]
print("Unsorted: ",arr)
# Calling the bubble sort function
print("Sorted: ",bubble_sort(arr))