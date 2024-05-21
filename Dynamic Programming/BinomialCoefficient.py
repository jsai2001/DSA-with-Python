# Time Complexity: 𝑂(𝑛)
# Space Complexity: 𝑂(1)
"""
The optimal way to calculate the binomial coefficient (𝑛/𝑘) is to avoid computing large factorials directly, 
which can be computationally expensive and prone to overflow for large values of n.
Instead, you can compute it iteratively using a multiplicative approach. 
This method is more efficient and numerically stable.

Here is a Python function that uses this optimal approach:
"""
def binomial_coefficient(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

# Example usage:
n = 5
k = 2
print(f"Binomial coefficient C({n}, {k}) = {binomial_coefficient(n, k)}")
"""
Explanation:
Symmetry Optimization: The binomial coefficient (𝑛/𝑘) is symmetric, meaning (𝑛/𝑘)=(𝑛/𝑛−𝑘). 
By choosing the smaller of 𝑘 and 𝑛−𝑘 , we minimize the number of iterations, which improves efficiency.
Iterative Calculation: Instead of calculating factorials, we use a loop to build up the result iteratively. 
This approach avoids the large intermediate values that factorials produce.
Integer Division: The calculation c * (n - i) // (i + 1) is performed using integer division to maintain precision and prevent overflow.

This method efficiently computes the binomial coefficient, making it suitable for large values of 𝑛 and 𝑘.

Simplifying the Formula
We can rewrite the binomial coefficient in a way that allows for incremental computation:

(𝑛/𝑘)=𝑛(𝑛−1)(𝑛−2)⋯(𝑛−𝑘+1)/𝑘(𝑘−1)(𝑘−2)⋯1

This is essentially breaking down the factorials and canceling out common terms in the numerator and the denominator.

Derivation of the Iterative Formula
To derive this formula, let's consider how the terms are built:

For 𝑖=0:
For 𝑖=1:
For 𝑖=2:

Generalizing this, we see that each term in the product can be computed iteratively using:

𝑐 = 𝑐 × (𝑛−𝑖)/(𝑖+1)

The time complexity and space complexity for the iterative approach using the formula 
𝑐 = 𝑐 × (𝑛−𝑖)/(𝑖+1) to compute the binomial coefficient are indeed 𝑂(𝑛) and 𝑂(1), respectively.

Time Complexity: 𝑂(𝑛)
The time complexity of the algorithm is determined by the number of iterations in the loop, which is proportional to the value of 𝑘. 
In the worst-case scenario, when 𝑘=𝑛/2 , the loop will execute 𝑛/2 times. Therefore, the time complexity is 𝑂(𝑛).

Space Complexity: 𝑂(1)
The space complexity refers to the amount of memory required by the algorithm, not including the input size. 
In this case, the algorithm uses only a constant amount of extra space for variables such as 𝑐, 𝑛, and 𝑘,
regardless of the input size. Therefore, the space complexity is 𝑂(1).
"""
