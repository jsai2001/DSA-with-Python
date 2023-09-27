def minimizeHeights(K,N,arr):
    if(N==1):
        return 0
    arr.sort()
    diff = arr[N-1] - arr[0]
    for i in range(1,N):
        if(arr[i]-K<0):
            continue
        minimum = min(arr[0]+K,arr[i]-K)
        maximum = max(arr[N-1]-K,arr[i-1]+K)
        diff    = min(diff,maximum-minimum)
    return diff
# print(minimizeHeights(3,5,[3,9,12,16,20]))
print(minimizeHeights(2,4,[1,5,8,10]))
