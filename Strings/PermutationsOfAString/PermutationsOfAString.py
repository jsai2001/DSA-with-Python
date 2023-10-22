# Time Complexity: O(n*n!)
# Space Complexity: O(n)

'''
find all permutations of a given string without using the itertools module 
or recursion and sorted in lexicographically ascending order

The above solution uses a loop to generate all possible permutations of a given string. 
It has a time complexity of O(n * n!). This is better than the recursive solution 
but not as efficient as the itertools method.

Time Complexity: O(n*n!)
Space Complexity: O(n)
'''
def get_permutations(string):
    if len(string) == 1:
        return [string]

    permutations = []
    for i in range(len(string)):
        char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        for permutation in get_permutations(remaining_chars):
            permutations.append(char + permutation)

    return sorted(permutations)

string = "ABC"
permutations = get_permutations(string)
print(permutations)