# Selection Sort algorithm
def selection(a): # Function to implement selection sort
    for i in range(len(a)): # Traverse through all array elements
        small = i # minimum element in unsorted array
        for j in range(i+1,len(a)):
            if a[small]>a[j]:
                small=j
        # Swap the found minimum element with the first element
        a[i] , a[small] = a[small] , a[i]

def printArr(a):
    for i in range(len(a)):
        print(a[i],end=' ')

a = [69, 14, 1, 50, 59]  
print("Before sorting array elements are - ")  
printArr(a)  

print("\nAfter sorting array elements are - ")  
selection(a)  
printArr(a)  