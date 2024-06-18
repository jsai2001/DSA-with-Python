### Rotate a Doubly Linked list in group of Given Size.

To solve the problem of reversing every group of \( k \) nodes in a doubly linked list, we can follow a systematic approach. Here is a step-by-step guide, complete with detailed explanations, code implementation, and analysis of time and space complexity.

- **Time Complexity:** \(O(N)\)

- **Space Complexity:** \(O(1)\)

### Explanation

A doubly linked list consists of nodes, each having three fields: a data field, a pointer to the previous node, and a pointer to the next node. Reversing every group of \( k \) nodes means we need to reverse the order of nodes within each group of \( k \) nodes while maintaining the overall structure of the list.

### Steps to Reverse Every Group of \( k \) Nodes

1. **Traverse the List in Chunks of \( k \) Nodes:**
   - Start from the head and count \( k \) nodes.
   - If the number of remaining nodes is less than \( k \), then there is no need to reverse the last group.

2. **Reverse Each Chunk:**
   - For each group of \( k \) nodes, reverse the pointers between the nodes.
   - Update the connections between the reversed group and the rest of the list.

3. **Adjust the Pointers:**
   - Ensure that the `prev` and `next` pointers of each node are correctly updated after reversing the nodes within each group.

### Time and Space Complexity

- **Time Complexity:** \( O(n) \)
  - Each node is processed exactly once, making the time complexity linear with respect to the number of nodes in the list.
- **Space Complexity:** \( O(1) \)
  - The algorithm performs the reversal in place, requiring no additional space proportional to the input size.

### Implementation

Here is a Python implementation of the described approach:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def reverse_group(head, k):
    if head is None or k == 1:
        return head

    current = head
    new_head = None
    ktail = None

    while current:
        count = 0
        current = head

        # Find the next group of k nodes
        while count < k and current:
            current = current.next
            count += 1
        
        # If we have k nodes, then we reverse them
        if count == k:
            rev_head = reverse_k_nodes(head, k)
            
            # new_head is the new head of the final list
            if not new_head:
                new_head = rev_head

            # ktail is the tail of the previous reversed group
            if ktail:
                ktail.next = rev_head
            head.prev = ktail
            ktail = head
            head = current
    
    # Attach the final, possibly un-reversed portion
    if ktail:
        ktail.next = head
        if head:
            head.prev = ktail

    return new_head if new_head else head

def reverse_k_nodes(head, k):
    current = head
    prev = None
    next = None
    count = 0

    while current and count < k:
        next = current.next
        current.next = prev
        current.prev = next
        prev = current
        current = next
        count += 1

    return prev

# Helper function to print the list (for testing)
def print_list(head):
    while head:
        print(head.data, end=' <=> ')
        head = head.next
    print('None')

# Helper function to create a doubly linked list from a list (for testing)
def create_doubly_linked_list(data_list):
    if not data_list:
        return None
    
    head = Node(data_list[0])
    current = head
    for data in data_list[1:]:
        new_node = Node(data)
        current.next = new_node
        new_node.prev = current
        current = new_node
    
    return head

# Example usage
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 3
    head = create_doubly_linked_list(data)
    print("Original List:")
    print_list(head)
    
    head = reverse_group(head, k)
    
    print("\nReversed in groups of 3:")
    print_list(head)
```

### Explanation of the Implementation

1. **Node Class:**
   - Represents a node in a doubly linked list.

2. **reverse_group Function:**
   - Main function to reverse every group of \( k \) nodes.
   - Iterates over the list, reversing nodes in groups of \( k \).
   - Maintains pointers to connect reversed groups properly.

3. **reverse_k_nodes Function:**
   - Reverses \( k \) nodes starting from a given head node.
   - Adjusts `next` and `prev` pointers to reverse the direction of the list segment.

4. **Helper Functions:**
   - `print_list` to display the list.
   - `create_doubly_linked_list` to create a list from an array for testing purposes.

This implementation efficiently reverses groups of \( k \) nodes in a doubly linked list, ensuring all pointers are correctly adjusted, and the time and space complexities are optimal.