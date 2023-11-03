'''
This code is for counting all the occurances of a search word , in rows and columns
'''
def count_occurrences(arr, word):
    count = 0
    for row in arr:
        joined_row = ''.join(row)
        count += joined_row.count(word)
        count += joined_row[::-1].count(word)
    for col in range(len(arr[0])):
        joined_col = ''.join([row[col] for row in arr])
        count += joined_col.count(word)
        count += joined_col[::-1].count(word)
    return count

arr = [
    ['D', 'D', 'D', 'G', 'D', 'D'],
    ['B', 'B', 'D', 'E', 'B', 'S'],
    ['B', 'S', 'K', 'E', 'B', 'K'],
    ['D', 'D', 'D', 'D', 'D', 'E'],
    ['D', 'D', 'D', 'D', 'D', 'E'],
    ['D', 'D', 'D', 'D', 'D', 'G']
]
word = 'GEEKS'
print(f"The word '{word}' appears {count_occurrences(arr, word)} times in the 2D character array.")