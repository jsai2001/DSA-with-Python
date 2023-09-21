# Time Complexity
# Regular => O(n)
# Best Case => O(n) 
#    => If the element that we want to find is n/2th element ,
#       and after one partition our i index present at n/2th index 
#       and n/2th element is present at pivot , which is last of the array
#       So, in one iteration , you are able to find the n/2th element
# Worst Case => O(n^2)
#    => In a sorted array , if we want to find 1st smallest element ,
#       We need to have pivot from the last of the array , and sort it 
#       to the first , where the array is already sorted, as we know , 
#       in first iteration , it iterates through n elements
#       in second iteration , it iterates through n-1 elements
#       in third iteration , it iterates through n-2 elements
#       So on...... , It takes O(n^2) worst case time complexity

# It is faster than Quick sort algorithm ,
# because Quick select remebers only one partition ,
# it only store the partition which is between high and low pointers.
def partition(arr,low,high):
    pivot = arr[high]
    i = low
    for j in range(low,high):
        if(arr[j]<=pivot):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[high]=arr[high],arr[i]
    return i

def kth_largest_element(arr,k):
    low = 0
    high = len(arr)-1
    while True:
        pivot_index = partition(arr,low,high)
        if pivot_index == len(arr) - k:
            return arr[pivot_index]
        elif pivot_index > len(arr) - k:
            high = pivot_index - 1
        else:
            low = pivot_index + 1

arr = [4, 2, 7, 1, 5, 9, 3]
k = 3
kth_largest = kth_largest_element(arr, k)
print(kth_largest)

# ------------------------------------------------------------------------
'''
The purpose of the partition function is to rearrange the elements of the array such that 
all elements less than or equal to the pivot are placed before it, 
and all elements greater than the pivot are placed after it. This process is known as partitioning.

Here’s a step-by-step breakdown of how the partition function works:

* The function takes three parameters: arr, low, and high. 
* arr is the input array, and low and high define the range of indices to consider.
* A pivot element is selected from the array. 
* In this implementation, the pivot is chosen as the last element (arr[high]).
* The function initializes an index i to low.
* The function iterates over the range from low to high - 1 using a variable j.
* For each element arr[j], if it is less than or equal to the pivot, it swaps arr[i] with arr[j] and increments i. 
* This ensures that all elements less than or equal to the pivot are moved to the left side of the partition.
* Finally, the pivot element is swapped with arr[i], placing it at its correct sorted position.
* The function returns the index of the pivot element.
* The purpose of this partitioning step is to divide the array into two parts: 
    * one with elements less than or equal to the pivot, and another with elements greater than the pivot.
    * This allows for efficient selection of elements based on their relative order.

In this example, we have an array arr with the values [4, 2, 7, 1, 5, 9, 3] and we want to find the 3rd largest element.

    * Here’s how the kth_largest_element function works step by step:
    * The initial values of low and high are set to 0 and len(arr) - 1, respectively.
    * The while loop starts and continues until the condition is met.
    * The partition function is called with the current values of low and high. 
    * It selects a pivot element and partitions the array around it.
    * If the pivot index (pivot_index) is equal to len(arr) - k, we have found the Kth largest element. 
    * In this example, if pivot_index is equal to 7 - 3 = 4, we have found the 3rd largest element.
    * If the pivot index is greater than len(arr) - k, we update high to be pivot_index - 1. 
    * This means that the Kth largest element is in the left partition of the array.
    * If the pivot index is less than len(arr) - k, we update low to be pivot_index + 1. 
    * This means that the Kth largest element is in the right partition of the array.
    * The loop continues until the condition is met, and finally, we return the Kth largest element.
    * In our example, the output will be 5, as it is the 3rd largest element in the array.
'''
# ------------------------------------------------------------------------