### Check preorder is valid or not

To determine if a given preorder traversal sequence can represent a valid Binary Search Tree (BST), we can use a stack-based approach. The key idea is to keep track of the current lower bound for the nodes. Here’s a detailed explanation along with time and space complexity analysis.

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(n)\)

## Algorithm Explanation

1. **Initialization**:
   - Create an empty stack.
   - Set a variable `lower_bound` to negative infinity.

2. **Traversal**:
   - Iterate through each value `val` in the preorder sequence.
   - For each value:
     - Check if `val` is less than the `lower_bound`. If it is, the sequence is invalid, and we return `False`.
     - While the stack is not empty and the top of the stack is less than `val`, pop the stack and update `lower_bound` to the value popped.
     - Push `val` onto the stack.

3. **Completion**:
   - If the loop completes without finding any invalid conditions, the sequence is valid, and we return `True`.

### Detailed Steps

1. **Initialization**:
   - `stack = []`
   - `lower_bound = float('-inf')`

2. **Traversal**:
   - For each `val` in `preorder`:
     - If `val < lower_bound`, return `False`.
     - While `stack` is not empty and `stack[-1] < val`:
       - Update `lower_bound = stack.pop()`.
     - Push `val` onto the `stack`.

3. **Completion**:
   - Return `True`.

### Example

Let's walk through an example:
Preorder sequence: `[5, 2, 1, 3, 6]`

- Start with an empty stack and `lower_bound = -inf`.
- Iterate through each value:
  - `val = 5`: Push 5 onto the stack. Stack: `[5]`
  - `val = 2`: Push 2 onto the stack. Stack: `[5, 2]`
  - `val = 1`: Push 1 onto the stack. Stack: `[5, 2, 1]`
  - `val = 3`: `3 > 1`, pop 1, update `lower_bound = 1`. `3 > 2`, pop 2, update `lower_bound = 2`. Push 3 onto the stack. Stack: `[5, 3]`
  - `val = 6`: `6 > 3`, pop 3, update `lower_bound = 3`. `6 > 5`, pop 5, update `lower_bound = 5`. Push 6 onto the stack. Stack: `[6]`
- All values processed, return `True`.

### Python Code

Here is the Python code to implement the above logic:

```python
def is_valid_preorder(preorder):
    stack = []
    lower_bound = float('-inf')
    
    for val in preorder:
        if val < lower_bound:
            return False
        while stack and stack[-1] < val:
            lower_bound = stack.pop()
        stack.append(val)
    
    return True

# Example usage:
preorder = [5, 2, 1, 3, 6]
print(is_valid_preorder(preorder))  # Output: True
```

### Time and Space Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes in the preorder sequence. Each element is pushed and popped from the stack at most once.
- **Space Complexity**: \(O(n)\) in the worst case for the stack. In the worst scenario, all elements are stored in the stack if the sequence is strictly decreasing.

This approach ensures that we efficiently check the validity of the preorder sequence for a BST using linear time and space.