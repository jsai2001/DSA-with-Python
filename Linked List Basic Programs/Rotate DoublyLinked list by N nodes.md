### Rotate DoublyLinked list by N nodes

Rotating a doubly linked list counter-clockwise by \( N \) nodes involves rearranging the pointers of the nodes such that the list starts from the \( N \)-th node and the nodes before the \( N \)-th node are moved to the end of the list. Let's go through a detailed explanation, including the steps to achieve this, and analyze the time and space complexity.

- **Time Complexity:** \(O(M)\)

- **Space Complexity:** \(O(1)\)

### Step-by-Step Solution:

1. **Identify the Node after Rotation**:
   - Traverse the list to find the \( N \)-th node. This node will become the new head of the list after rotation.

2. **Adjust Pointers**:
   - Set the new head's previous pointer (`prev`) to `None`.
   - The node just before the \( N \)-th node (let's call it the \( (N-1) \)-th node) will have its next pointer set to `None`, making it the new tail of the list.
   - Traverse to the end of the list to find the current tail.
   - Set the current tail's next pointer to the original head.
   - Set the original head's previous pointer to the current tail.

3. **Return the New Head**:
   - Update the head of the list to the \( N \)-th node.

### Detailed Steps:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def rotate_doubly_linked_list(head, N):
    if head is None or N <= 0:
        return head
    
    # Step 1: Traverse the list to find the N-th node
    current = head
    count = 1
    while count < N and current is not None:
        current = current.next
        count += 1
    
    # If the N is greater than or equal to the length of the list
    if current is None:
        return head
    
    # The N-th node
    NthNode = current
    
    # Step 2: Adjust pointers to rotate the list
    if NthNode.next is not None:
        # Break the link before the N-th node
        if NthNode.prev is not None:
            NthNode.prev.next = None
        NthNode.prev = None

        # Find the tail of the list
        tail = NthNode
        while tail.next is not None:
            tail = tail.next

        # Connect the old tail to the old head
        tail.next = head
        head.prev = tail
    
    return NthNode
```

### Explanation:

1. **Initialization**:
   - A `Node` class is defined with data, next, and prev attributes.
   - The `rotate_doubly_linked_list` function is defined to perform the rotation.

2. **Traverse to Find the \( N \)-th Node**:
   - Start from the head and move \( N \) steps forward to find the \( N \)-th node.
   - Ensure \( N \) is valid (not greater than the list length).

3. **Adjust Pointers**:
   - Break the link between the \( (N-1) \)-th node and the \( N \)-th node.
   - Traverse to the end to find the current tail and link it to the original head.
   - Update the previous pointers accordingly.

4. **Return the New Head**:
   - The \( N \)-th node becomes the new head of the list.

### Time Complexity:

- **Traversal to find the \( N \)-th node**: \( O(N) \)
- **Traversal to find the tail of the list**: \( O(M-N) \) where \( M \) is the total number of nodes in the list.
- **Overall Time Complexity**: \( O(M) \) where \( M \) is the total number of nodes in the list.

### Space Complexity:

- **Space Complexity**: \( O(1) \) since no extra space proportional to the input size is used; only a few pointers are utilized.

This solution efficiently rotates the doubly linked list in linear time with constant space.