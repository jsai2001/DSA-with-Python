# Kth Largest Element in an array

We will be discussing various methods to find Kth Largest Element of the array

## Method 1

* First we need to sort the array using merge sort
* And then return the (n-K)th element of the sorted array
* And if we want to return Kth minimum element of array return the (K-1)th element
* Time complexity of this method , is for performing merge sort it takes O(NlogN) and for retrieving some xth element it takes O(1) time , so the overall complexity is O(NlogN)

## Method 2

* While we are using max heap , we need to return the kth retrival of the max heap tree , which will be already sorted in decending order , but if we wanted to acheive the same with the min heap , we need to retrieve (n-k+1)th element of the min heap tree.

![TimeComplexity Analysis while using Heaps](./Common_Images/img_1.png "TimeComplexity Analysis while using Heaps")

* If we use max heap to find Kth largest element , then we would require O(N) time for building a heap and after pulling out top most element which is largest from the heap , we need to re-heapify the array , which would take logN times , and we does this re-heapification K times , as we gonna re-heap K times and pull the top most element from the heap. Overall It would take O(N+KlogN)
* If we use min heap for finding Kth largest element , it would take O(N+(N-K+1)log(N-K+1)) , because we do remove element and re-heapify N-K+1 times , as we need to remove the N-K+1 elements from the first to get the Kth Largest element using min-heap.