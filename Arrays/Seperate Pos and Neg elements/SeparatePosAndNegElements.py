def seperate(arr):
    low=0
    high=len(arr)-1
    while low<=high:
        if arr[low]<0:
            low+=1
        elif arr[low]>0 and arr[high]<0:
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high-=1
        else:
            high-=1
    return arr
print(seperate([1, 2,  -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2,  1]))
