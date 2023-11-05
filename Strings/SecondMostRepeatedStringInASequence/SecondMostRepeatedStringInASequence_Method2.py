# Time Complexity: O(n)
# Space Complexity: O(n*max(|Si|)
'''
Basically , we need are creating counter of elements of the array into a dictionary
And creating two different , pointers for first maximum element count and the second maximum element count
Returning the second maximum element count , by iterating through the dictionary.
'''
import sys
def secFrequent(arr, n):
        dick = dict()
        for i in range(len(arr)):
            if arr[i] not in dick:
                dick[arr[i]]=1
            else:
                dick[arr[i]]+=1
        firstmax = -sys.maxsize-1
        secondmax = -sys.maxsize-1
        for i in dick.values():
            if(i>firstmax and secondmax!=-sys.maxsize-1):
                secondmax = firstmax
                firstmax = i
            elif(i>firstmax):
                firstmax = i
            elif(i>secondmax):
                secondmax = i
        for key,value in dick.items():
            if(value==secondmax):
                return key
n=6
arr = "geeks for geeks for geeks aaa".split()
print(secFrequent(arr,n))