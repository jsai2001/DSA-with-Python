### Removing duplicate elements from an unsorted Linked List

To solve the problem of removing duplicate elements from an unsorted linked list while keeping the first occurrence of each element, we can use the following approach:

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(n)\)

### Approach

1. **Traverse the linked list**: We need to iterate through each node in the linked list.
2. **Track seen values**: Use a hash set to keep track of values that have already been seen.
3. **Remove duplicates**: If a value is encountered that is already in the hash set, remove the node from the linked list. If it is not in the hash set, add it to the hash set and continue.

### Steps

1. **Initialize a hash set**: This will store the values that have been encountered as we traverse the linked list.
2. **Initialize pointers**: Use two pointers, `current` to traverse the linked list and `prev` to keep track of the previous node.
3. **Traverse the list**: For each node, check if the value exists in the hash set.
   - If it exists, adjust the pointers to remove the node.
   - If it does not exist, add the value to the hash set and move the pointers forward.
4. **Update pointers**: Continue this process until the end of the linked list is reached.

### Pseudocode

```python
def remove_duplicates(head):
    if head is None:
        return None
    
    seen_values = set()  # Set to store seen values
    current = head
    prev = None
    
    while current is not None:
        if current.data in seen_values:
            # Duplicate found, remove it
            prev.next = current.next
        else:
            # Not a duplicate, add to seen values
            seen_values.add(current.data)
            prev = current
        current = current.next
    
    return head
```

### Detailed Explanation

1. **Edge case**: If the linked list is empty (i.e., head is `None`), return `None` as there are no nodes to process.
2. **Initialization**: 
   - `seen_values` is a set that keeps track of all the unique values encountered so far.
   - `current` is initialized to `head` to start the traversal from the beginning of the linked list.
   - `prev` is initially set to `None` and will trail behind `current` to help with node removal.
3. **Traversal and duplication check**:
   - Iterate through the linked list using `current`.
   - For each node, check if `current.data` is in `seen_values`.
     - If it is, set `prev.next` to `current.next` to bypass the current node, effectively removing it from the linked list.
     - If it is not, add `current.data` to `seen_values` and move `prev` to `current`.
   - Move `current` to the next node (`current = current.next`).
4. **Return the modified linked list**: After processing all nodes, the head of the modified linked list is returned.

### Time Complexity

- **O(N)**: Each node in the linked list is visited exactly once, where \( N \) is the number of nodes in the linked list.
- Insertion and lookup operations in a hash set are \( O(1) \) on average.

### Space Complexity

- **O(N)**: In the worst case, if all elements are unique, the hash set will store all \( N \) elements.

### Example

Suppose the linked list is `4 -> 2 -> 4 -> 3 -> 2 -> 1 -> 3`.

1. Initialize `seen_values = {}`.
2. Start traversal:
   - Node `4`: Not in `seen_values`, add `4` (`seen_values = {4}`).
   - Node `2`: Not in `seen_values`, add `2` (`seen_values = {4, 2}`).
   - Node `4`: In `seen_values`, remove it.
   - Node `3`: Not in `seen_values`, add `3` (`seen_values = {4, 2, 3}`).
   - Node `2`: In `seen_values`, remove it.
   - Node `1`: Not in `seen_values`, add `1` (`seen_values = {4, 2, 3, 1}`).
   - Node `3`: In `seen_values`, remove it.
3. Resultant linked list: `4 -> 2 -> 3 -> 1`.

### Conclusion

This method effectively removes duplicate elements from an unsorted linked list while maintaining the order of first occurrences. The use of a hash set allows for efficient detection of duplicates, making the solution both time and space efficient.