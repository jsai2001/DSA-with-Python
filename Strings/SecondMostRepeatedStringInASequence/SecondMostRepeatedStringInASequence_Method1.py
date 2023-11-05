def secFrequent(arr, n):
    dick = dict()
    for i in range(len(arr)):
        if arr[i] not in dick:
            dick[arr[i]]=1
        else:
            dick[arr[i]]+=1
    sorteddick = dict(sorted(dick.items(),key=lambda item:item[1],reverse=True))
    sortedlist = list(sorteddick.items())
    return sortedlist[1][0]
n=6
arr = "aaa bbb ccc bbb aaa aaa".split()
print(secFrequent(arr,n))
