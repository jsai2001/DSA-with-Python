'''
Search a Word in a 2D Grid of characters (Word Search)

Given a 2D grid of characters and a single word/an array of words, 
find all occurrences of the given word/words in the grid. 
A word can be matched in all 8 directions at any point. 
Word is said to be found in a direction if all characters match in this direction (not in zig-zag form).

The 8 directions are, Horizontally Left, Horizontally Right, Vertically Up, 
Vertically Down and 4 Diagonal directions.
'''
def search2D(grid,row,col,word,R,C):
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]
    if grid[row][col]!=word[0]:
        return False
    length = len(word)
    for direction in range(8):
        k = 1
        rd = row + x[direction]
        cd = col + y[direction]
        while k < length and 0<=rd<R and 0<=cd<C:
            if grid[rd][cd] != word[k]:
                break
            rd += x[direction]
            cd += y[direction]
            k += 1
        if k == length:
            return True
    return False

def patternSearch(grid,word,R,C):
    result = list()
    for row in range(R):
        for col in range(C):
            if search2D(grid,row,col,word,R,C):
                result.append([row,col])
    return result
R = 3
C = 13
grid = [
    ["G", "E", "E", "K", "S", "F", "O", "R", "G", "E", "E", "K", "S"],
    ["G", "E", "E", "K", "S", "Q", "U", "I", "Z", "G", "E", "E", "K"],
    ["I", "D", "E", "Q", "A", "P", "R", "A", "C", "T", "I", "C", "E"]
]
word = "GEEKS"
print(f"{word} === {patternSearch(grid, word, R, C)}")
word = "EEE"
print(f"{word} === {patternSearch(grid, word, R, C)}")
grid_1 = [['a','b','a','b'],['a','b','e','b'],['e','b','e','b']]
word_1 = "abe"
print(f"{word} === {patternSearch(grid_1, word_1, len(grid_1), len(grid_1[0]))}")
'''
The time complexity of the Word Search algorithm is O(N * M * 8^L), 
where N is the number of rows, M is the number of columns, 
and L is the length of the word we are searching for. 
This is because we are searching for the given word in all possible directions from each cell in the grid, 
which takes O(8 * L) time. 

Since there are N * M cells in the grid, 
the time complexity of the algorithm is O(N * M * 8^L).

The space complexity of the algorithm is O(1), 
as we are not using any additional data structures to store the grid or the word. 
We are only using a few variables to keep track of the current cell and the direction of search.
'''