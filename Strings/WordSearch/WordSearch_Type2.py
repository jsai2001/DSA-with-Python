'''
Search the word in all possible directions

Algorithm:

Step 1– Traverse matrix character by character and take one character as string start 
Step 2– For each character find the string in all the four directions recursively 
Step 3– If a string found, we increase the count 
Step 4– When we are done with one character as start, we repeat the same process for the next character 
Step 5– Calculate the sum of count for each character 
Step 6– Final count will be the answer
'''

'''
We basically have a variable found initialized to 0 in the recursive stack
And iterate in all directions to find the string that we want
We basically increase iterate in all directions for searching the next character of the word
only if we find the first character in the char array
If current character of the word matches with what we have in the grid
We increase the iterator which is pointing to the characters of the word ,
and searches for other characters of the word that we want to match in all four directions.
And if the iterator which is pointing to the word , gets to an end , we return found as 1,
which accumulate the count of the found variable in recursion stack.
Finally the found variable will be returned by solve function , by checking number of words
found in chararray from the current index i,j

And we use this solve function for all (i,j) in chararray,
Finally we accumulate the result in ans variable and print it

We are initialising chararray[i][j] as 0 , when chararray[i][j] is matching the word[idx],
because , when we furthur iterate in all directions , for searching the next character , 
we should not iterate back to the same word , that we have just searched or visited.
It is something like visited or not array.

After searching recursivily to all directions from i,j , we will be filling back with the characters
Where we have filled with 0 earlier.
'''
def solve(i,j,word,chararray,size,idx):
    found = 0
    if(i>=0 and j>=0 and i<len(chararray) and j<len(chararray[0]) and word[idx]==chararray[i][j]):
        temp = word[idx]
        chararray[i][j] = 0
        idx += 1
        if(idx == size):
            found = 1
        else:
            found += solve(i+1,j,word,chararray,size,idx)
            found += solve(i-1,j,word,chararray,size,idx)
            found += solve(i,j+1,word,chararray,size,idx)
            found += solve(i,j-1,word,chararray,size,idx)
        chararray[i][j] = temp
    return found    

word = "MAGIC"
chararray = ["BBABBM","CBMBBA","IBABBG",
        "GOZBBI","ABBBBC","MCIGAM"]
chararray = [[j for j in i] for i in chararray]
print(chararray)
ans = 0
size = len(word)
for i in range(len(chararray)):
    for j in range(len(chararray[0])):
        ans += solve(i,j,word,chararray,size,0)
print(f"The word {word} present {ans} times in the chararray")
'''
Time complexity of the solve() function is O(n^2 * m^2), 
where n is the row size and m is the column size of the character array 1. 
This is because the function recursively explores all possible paths in the character array to find the word. 
Since each character has 4 possible directions to explore, the time complexity is exponential.

Space Complexity: O(nm)
'''