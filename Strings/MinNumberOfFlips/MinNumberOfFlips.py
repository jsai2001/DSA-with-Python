'''
Given a binary string, that is it contains only 0s and 1s. 
We need to make this string a sequence of alternate characters by flipping some of the bits, 
our goal is to minimize the number of bits to be flipped.

We are trying to match S with even binary string (01010101) and odd binary string (10101010)
And count number of mismatches from even binary string through evenCheck
And count number of mismatches from odd binary string through oddCheck
And return minimum of them

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
'''
def minFlips(S):
    evenCheck = 0
    oddCheck = 0
    for i in range(len(S)):
        if(i%2==0 and S[i]=='1'):
            evenCheck += 1
        elif(i%2!=0 and S[i]=='0'):
            evenCheck += 1
        if(i%2==0 and S[i]=='0'):
            oddCheck += 1
        elif(i%2!=0 and S[i]=='1'):
            oddCheck += 1
    return min(evenCheck,oddCheck)
print("""MinFlips for 001: """+str(minFlips("001"))) # 1
print("""MinFlips for 0001010111: """+str(minFlips("0001010111"))) # 2