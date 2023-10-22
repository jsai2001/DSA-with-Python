import itertools
def find_permutation(S):
    return ["".join(i) for i in list(set(itertools.permutations(S)))]
string = "ABC"
print(find_permutation(string))