'''
Time Complexity : O(m) 
We need to consider length of arr2 , 
because we are computing the subset based on arr2 through arr1

Space Complexity : O(n)
'''
from collections import Counter
def isSubset( a1, a2, n, m):
    a1count = Counter(a1)
    a2count = Counter(a2)
    for i in a2count:
        if i not in a1count or a2count[i]>a1count[i]:
            return "No"
    return "Yes"
arr1 = [1, 2, 3, 4, 4, 5, 6]
arr2 = [1, 2, 4]
n = len(arr1)
m = len(arr2)
print(isSubset(arr1,arr2,n,m))