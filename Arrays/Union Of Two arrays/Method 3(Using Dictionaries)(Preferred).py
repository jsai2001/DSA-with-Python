# Expected Time Complexity : O(n+m)
# Expected Auxilliary Space : O(n+m)

def doUnion(a,n,b,m):
    book=dict()
    for i in range(len(a)):
        if a[i] not in book:
            book[a[i]]=1
        else:
            book[a[i]]+=1
    for i in range(len(b)):
        if b[i] not in book:
            book[b[i]]=1
        else:
            book[b[i]]+=1
    return len(book)
print(doUnion([85,25,1,32,54,6],6,[85,2],2))