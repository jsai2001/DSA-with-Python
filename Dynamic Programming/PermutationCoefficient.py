# Time Complexity O(n)
# Space Complexity O(1)
"""
nCr and nPr represent two different ways of counting arrangements of objects, 
but the key difference lies in whether the order of the objects matters.

nPr (Permutation):

This refers to the number of ways to arrange r objects chosen from a set of n objects when the order matters.
Imagine you have 3 different letters (n = 3) and you want to find how many unique arrangements (order matters) you can make with 2 of them (r = 2). 
The answer (nPr) would be the number of combinations like AB, BA, etc.
The formula for nPr is: nPr = n! / (n-r)!

nCr (Combination):

This refers to the number of ways to select r objects from a set of n objects when the order doesn't matter.
Going back to the 3 letter example (n = 3), if you only care about choosing 2 of them (r = 2), 
and not the order (AB is the same as BA), then nCr would tell you how many unique selections you can make.
The formula for nCr is: nCr = n! / (r! * (n-r)!)
Here's an analogy:

Think of n objects as cupcakes and you want to choose r of them.
nPr is like arranging the chosen cupcakes in a row (order matters).
nCr is like simply picking out r cupcakes from a box (order doesn't matter).

Here's an optimized approach to calculate the permutation coefficient (nPr) in Python:
"""
def permutation_coefficient_optimized(n, r):
    """
  This function calculates the permutation coefficient (nPr) using a loop for better efficiency.

  Args:
      n: The total number of objects.
      r: The number of objects to choose.

  Returns:
      The permutation coefficient (nPr).
  """
    if r == 0:
        return 1
    result = 1
    for i in range(n, n-r, -1):
        result *= i
    return result

# Example usage
n = 4
r = 2
result = permutation_coefficient_optimized(n, r)
print(f"The permutation coefficient P({n}, {r}) is: {result}")
"""
This code utilizes a loop for better efficiency compared to the recursive approach. It works as follows:

Base Case: Similar to the previous approach, if r is 0, it returns 1.
Loop: It initializes a variable result to 1. Then, it iterates from n down to n-r+1 (n minus r) using a loop.
Calculation: Inside the loop, it multiplies the current value of result with the current loop variable i. 
This essentially calculates n * (n-1) * (n-2) * ... * (n-r+1).
This approach avoids the overhead of function calls associated with recursion and directly calculates the factorial involved in nPr. 
It offers significant performance improvement for larger values of n and r.
"""
"""
Time Complexity (O(n)):

The loop iterates a maximum of r times (from n down to n-r+1).
Each iteration involves a constant time multiplication operation.
Therefore, the total number of operations is proportional to r, 
which in the worst case is n (when r = n). This makes the time complexity linear in n.

Space Complexity (O(1)):

The function uses a constant amount of extra space for variables like result and i.
These variables do not depend on the input size (n and r).
So, the space complexity remains constant regardless of the input, making it O(1).
"""
