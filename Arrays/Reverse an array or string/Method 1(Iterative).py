# Iterative python program to reverse an array

# Function to reverse A[] from start to end
def reverseList(A,start,end):
    while start < end:
        A[start],A[end] = A[end],A[start]
        start += 1
        end -= 1

A = [1,2,3,4,5,6]
print("Original list is")
print(A)
reverseList(A,0,5)
print("Reversed list is")
print(A)

'''
----------------------------
Output:
----------------------------
Original list is
[1, 2, 3, 4, 5, 6]
Reversed list is
[6, 5, 4, 3, 2, 1]
----------------------------

Time Complexity: O(n)
Auxilary Space: O(1)
'''