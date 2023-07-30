# Recursive python program to reverse an array
# Function to reverse A[] from start to end
def reverseList(A,start,end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A,start+1,end-1)

A = [1, 2, 3, 4, 5, 6]
print("Original array:")
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)

'''
-----------------------
Output:
-----------------------
Original array:
[1, 2, 3, 4, 5, 6]
Reversed list is
[6, 5, 4, 3, 2, 1]
-----------------------

Time Complexity: O(n)
Auxilary Space: O(n), due to recursive call stack
'''