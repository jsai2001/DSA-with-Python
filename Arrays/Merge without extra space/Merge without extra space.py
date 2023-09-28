# Time Complexity: O((N+M) * log(N+M))
# Auxiliary Space: O(1)
arr1=[1, 5, 9, 10, 15, 20]
arr2=[2, 3, 8, 13]
n=6
m=4
def merge(n,m):
    i=0
    j=0
    k=n-1
    global arr1
    global arr2
    while(j<m and k>i):
        if(arr1[i]<arr2[j]):
            i+=1
        elif(arr1[i]>arr2[j]):
            arr1[k],arr2[j]=arr2[j],arr1[k]
            j+=1
            k-=1
    arr1.sort()
    arr2.sort()
merge(n,m)
print("Sorted Array would be : ",arr1+arr2)