'''
Time Complexity: O(N), Traversing the array of size N.
Auxiliary Space: O(N), Space occupied by the hashmap

We can solve this question using sorting in O(nlogn) Time Complexity , 
O(nlogn) for sorting and O(n) for linear traversal to check the counts
and print result. => O(nlogn)+O(n) = O(nlogn)

We are also having a solution for this question to find it in O(N^2) TC,
Where one for loop is used to fix a number in an array , and inner for loop
is used to count number of occurances of that number in the array , and give
the result. Following hashing technique is the better among all.
'''


# Python3 code to find elements whose
# frequency is more than n/k
def morethanNbyK(arr,n,k):
    x = n//k
    # unordered_map initialization
    freq = dict()
    # Accumulate frequency
    for i in range(len(arr)):
        if arr[i] not in freq:
            freq[arr[i]] = 1
        else:
            freq[arr[i]] += 1
    # Traverse the map to find elements which have freq > n/k
    for i in freq:
        # Checking if value of key-value pair is greater than x (x=n/k)
        if(freq[i]>x):
            # Print key of whose value is greater than x
            print(i)
arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
n = len(arr)
k = 4 
morethanNbyK(arr, n, k)