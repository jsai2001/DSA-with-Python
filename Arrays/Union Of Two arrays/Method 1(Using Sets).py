def doUnion(a,n,b,m):
    return len(set(a).union(set(b)))
print(doUnion([85,25,1,32,54,6],6,[85,2],2))
