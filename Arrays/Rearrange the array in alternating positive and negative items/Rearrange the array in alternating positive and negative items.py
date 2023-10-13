# Time Complexity : O(n^2)
# Auxilary Space: O(1)
def rearrange(arr,n):
    i=0
    j=n-1
    while(i<j):
        while(i<=n-1 and arr[i]>0):
            i+=1
        while(j>=0 and arr[j]<0):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    if(i==0 or i==n):
        return
    i+=1
    k=0
    while(k<n and i<n):
        arr[i],arr[k]=arr[k],arr[i]
        i+=1
        k+=2
    return arr
arr = list(map(int,"-5 -2 5 2 4 7 1 8 0 -8".split()))
n = len(arr)
print(rearrange(arr,n))