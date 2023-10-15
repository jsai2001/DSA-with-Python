# Time Complexity: O(n^2)
# Space Complexity: O(1)
def find3Numbers(A, n, X):
    A.sort() # Sorting takes O(nlogn) Time Complexity
    resultFlag = 0
    # Iterate through array from start to n-2 , 
    # We iterate until n-2 , because , we are finding triplets
    # It mean We have to find set of three numbers , 
    # But for last two numbers , there won't be a set pair of 3 , 
    # So we need to iterate until n-2th element
    for i in range(n-2):
        l = i+1
        r = n-1
        while(l<r):
            if(A[i]+A[l]+A[r]==X):
                resultFlag = 1
                break
            elif(A[i]+A[l]+A[r]<X): 
                '''
                If the sum is lower , we need to increase left , 
                because increasing from the left , increases the triplet sum , 
                hence we can match it to the X
                '''
                l+=1
            else: 
                '''
                Decreasing from the right makes the triplet sum to decrease , 
                so we can match the sum to X
                '''
                r-=1
        if(resultFlag==1): #We found triplet sum , hence exit , as we already found
            break
    return resultFlag

arr = list(map(int,"1 2 4 3 6".split()))
n = len(arr)
X = 10
if(find3Numbers(arr,n,X)):
    print("Found Triplet Sum!!!!")
else:
    print("Didn't found Triplet sum!!!!")