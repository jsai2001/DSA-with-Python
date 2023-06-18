# Counting sort in python
def countingSort(array):
    size = len(array)
    output = [0]*size
    # Initialize count array
    count = [0]*10
    # Store the count of each elements in count array
    for i in range(0,size):
        count[array[i]]+=1
    # Store the cummulative count
    # Here we are converting the count array to cummulative count array
    for i in range(1,10):
        count[i]+=count[i-1]
    # Find the index of each element of the original array in cummulative count array
    # place the elements in output array
    # after placing an element in output array , we must decrease the cummulative count of that index
    # so that , next time same element at different index of original array occurs , we will avoid substitution
    # of earlier element with current element , as both values are same
    i = size - 1
    while(i>=0):
        output[count[array[i]]-1] = array[i]
        count[array[i]] -= 1
        i -= 1
    # Copy the sorted elements into original array
    for i in range(0,size):
        array[i] = output[i]
data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
    