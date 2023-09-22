from collections import Counter
def doUnion(a,n,b,m):
    a.extend(b)
    result=Counter(a)
    return(len(result))
print(doUnion([85,25,1,32,54,6],6,[85,2],2))