# Time Complexity : O(n)
# Space Complexity : O(1)
def MinCharsToAddForPalin(text):
    n = len(text)
    i = 0
    j = n - 1
    last_index = n - 1
    while i <= j:
        if text[i] == text[j]:
            """
            Used to check adjacents satisfy palindomic condition or not
            If yes , move inwards to check furthur ,
            as they are satisfying the palindromic condition or not
            """
            i += 1
            j -= 1
        else:
            """
            Else , consider the last character is not part of the palindrome
            and check the palindromic condition from i=0 to last_index-1
            Here we are decrementing last_index , because ,
            we are eliminating the last index , and trying to check palin condition for
            (i,j) => (0,last_index-1) characters
            """
            i = 0
            last_index -= 1
            j = last_index
    added = n - 1 - last_index
    return added


text = "abc"
print(
    f"Minimum number of characters to be added to front to make {text} as Palindrome: {MinCharsToAddForPalin(text)}"
)
