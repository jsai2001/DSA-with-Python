import heapq

def kth_max_element(lst,k):
    # Create a max heap
    max_heap = [-x for x in lst]
    heapq.heapify(max_heap)
    # Extract the k-1 maximum elements
    for _ in range(k-1):
        heapq.heappop(max_heap)
    # Return the kth maximum element
    return -heapq.heappop(max_heap)

lst = [20, 15, 18, 8, 10, 5, 17]
k = 4
kth_max = kth_max_element(lst, k)
print(kth_max)

# ---------------------------------------------------------------------
'''
This implementation uses the heapq module from the Python standard library 
to create and manipulate the max heap. The time complexity of this approach 
is O(k * log n), where n is the size of the list.

K is the value which we give to find Kth largest element/smallest element

n is number of elements in the array

In general heapify function min heaps the array , so we are negating the values 
of the list , so the output will be given as max heap , and then we can return
Kth largest element from start , else we can also find Kth smallest element ,
If we not negate the values of the list.
'''
# ---------------------------------------------------------------------