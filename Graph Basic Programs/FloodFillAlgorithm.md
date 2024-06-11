## Flood Fill Algorithm

The Flood Fill algorithm is commonly used in computer graphics to determine the area connected to a given node in a multi-dimensional array. It's akin to the "bucket fill" tool in paint programs.

Here is a detailed implementation of the Flood Fill algorithm in Python using both Depth-First Search (DFS) and Breadth-First Search (BFS), along with an analysis of their time and space complexities.

- **Time Complexity:** \(O(N x M)\)
- **Space Complexity:** \(O(N x M)\)
### Depth-First Search (DFS) Implementation

```python
def flood_fill_dfs(image, sr, sc, new_color):
    """
    Perform a flood fill on the image starting from the pixel (sr, sc) using DFS.

    Parameters:
    - image (List[List[int]]): The 2D array representing the image.
    - sr (int): The row index of the starting pixel.
    - sc (int): The column index of the starting pixel.
    - new_color (int): The new color to fill the area with.

    Returns:
    - List[List[int]]: The image after performing the flood fill.
    """

    def dfs(x, y, color):
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != color:
            return
        image[x][y] = new_color
        dfs(x + 1, y, color)
        dfs(x - 1, y, color)
        dfs(x, y + 1, color)
        dfs(x, y - 1, color)

    if image[sr][sc] == new_color:
        return image

    original_color = image[sr][sc]
    dfs(sr, sc, original_color)
    return image

# Example usage
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr = 1
sc = 1
new_color = 2
print(flood_fill_dfs(image, sr, sc, new_color))
```

### Breadth-First Search (BFS) Implementation

```python
from collections import deque

def flood_fill_bfs(image, sr, sc, new_color):
    """
    Perform a flood fill on the image starting from the pixel (sr, sc) using BFS.

    Parameters:
    - image (List[List[int]]): The 2D array representing the image.
    - sr (int): The row index of the starting pixel.
    - sc (int): The column index of the starting pixel.
    - new_color (int): The new color to fill the area with.

    Returns:
    - List[List[int]]: The image after performing the flood fill.
    """
    
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    if original_color == new_color:
        return image

    queue = deque([(sr, sc)])
    image[sr][sc] = new_color

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == original_color:
                image[nx][ny] = new_color
                queue.append((nx, ny))

    return image

# Example usage
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr = 1
sc = 1
new_color = 2
print(flood_fill_bfs(image, sr, sc, new_color))
```

### Analysis

#### Time Complexity
For both DFS and BFS, the time complexity is \(O(N x M)\), where \(N\) is the number of rows and \(M\) is the number of columns in the image. This is because, in the worst case, we might have to visit every pixel in the image.

#### Space Complexity
- **DFS**: The space complexity is \(O(N x M)\) in the worst case due to the recursive stack.
- **BFS**: The space complexity is also \(O(N x M)\) in the worst case due to the queue.

In summary, both DFS and BFS have the same time and space complexity. However, BFS might be preferred in scenarios where recursion depth might exceed stack limits, making BFS more memory efficient in practical implementations for very large images.