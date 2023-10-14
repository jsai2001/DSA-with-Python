# Time complexity: O(n)
# Space complexity: O(n)
def subArrayExists(arr,n):
    ##Your code here
    flag=0
    if(arr.count(0)):
        return True
    else:
        prefixsum=[]
        prefixsum.append(arr[0])
        for i in range(1,len(arr)):
            prefixsum.append(prefixsum[i-1]+arr[i])
        if(len(prefixsum)!=len(set(prefixsum)) or prefixsum.count(0)):
            return True
        else:
            return False
arr = list(map(int,"4 2 -3 1 6".split()))
n = len(arr)
if(subArrayExists(arr,n)):
    print("Sub array exists with sum 0")
else:
    print("Sub array doesn't exists with sum 0")