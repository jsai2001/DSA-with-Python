# Heap Sort in Python
"""
Time Complexity
* Best Case: O(nlogn)
* Worst Case: O(nlogn)
* Average Case: O(nlogn)

Space Complexity => O(1)
"""
def heapify(arr,n,i):
    # Find the largest among root and children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    """
    If root is not largest , swap with largest and 
    continue heapifying from the node that we swapped with the root node
    Basically , we check does the tree follows max heap and
    if it does not , making sure that follows max heap by swapping the largest
    element with the root which is not largest than some of it's children
    which typically violates the max heap property. And heapify from the node 'largest'
    after the swapping. which heapify the whole tree and ensure that the tree or array 
    follows the max heap property.
    """
    if largest != i:
        arr[i] , arr[largest] = arr[largest] , arr[i]
        heapify(arr,n,largest)
def heapSort(arr):
    n = len(arr)
    '''
    Here n//2 denotes the right most non leaf node
    or we can also say that it gives the index of parent of last leaf node
    '''
    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1,0,-1):
        # Swap the largest valued node (root node)  of max heap
        # with the last element of unsorted array
        # array size decreases by 1 in every iteration ,
        # as in each iteration , we are going to have one sorted element at last of the array
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify root element
        heapify(arr, i, 0)
arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d " % arr[i], end='')