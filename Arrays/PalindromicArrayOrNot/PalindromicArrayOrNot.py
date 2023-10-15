# Time Complexity: O(n)
# Space Complexity: O(1)
def PalinArray(arr ,n):
    flag = 0
    for i in arr:
        if str(i) != str(i)[::-1]:
            flag = 1
            break
    if(flag==1):
        return 0
    return 1
n = 5
arr = [111,222,333,444,555]
if(PalinArray(arr,n)):
    print("It is Palindrome Array")
else:
    print("Not a Palindrome Array")