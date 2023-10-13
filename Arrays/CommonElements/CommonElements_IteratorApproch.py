#Method 1: Iterator Approach
#Time Complexity: O(n1+n2+n3)
#Space Complexity: O(1)
#       We are not taking any extra space as temp ,
#       We are only using an array to return to the program
def commonElements (A, B, C, n1, n2, n3):
        i=j=k=0
        commonElements=[]
        while(i<n1 and j<n2 and k<n3):
            if(A[i]==B[j] and B[j]==C[k] and A[i] not in commonElements):
                commonElements.append(A[i])
                i+=1
                j+=1
                k+=1
            else:
                if(A[i]<B[j] and A[i]<C[k]):
                    i+=1
                elif(B[j]<C[k] and B[j]<A[i]):
                    j+=1
                elif(C[k]<B[j] and C[k]<A[i]):
                    k+=1
                elif(A[i]==B[j]):
                    i+=1
                    j+=1
                elif(A[i]==C[k]):
                    i+=1
                    k+=1
                elif(B[j]==C[k]):
                    j+=1
                    k+=1
                else:
                    i+=1
                    j+=1
                    k+=1
        return commonElements
n1,n2,n3=list(map(int,"6 5 8".split()))
A=list(map(int,"1 5 10 20 40 80".split()))
B=list(map(int,"6 7 20 80 100".split()))
C=list(map(int,"3 4 15 20 30 70 80 120".split()))
print(commonElements(A, B, C, n1, n2, n3))