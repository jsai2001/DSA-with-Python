### Sort a “k” sorted Doubly Linked list

Solve the problem of sorting a doubly linked list where each node is at most \( k \) positions away from its target position, we can leverage a modified version of the insertion sort algorithm, which is well-suited for this specific scenario.

- **Time Complexity:** \( O(nk) \)

- **Space Complexity:** \( O(1) \)

### Detailed Explanation

#### Problem Understanding

Given:
- A doubly linked list with \( n \) nodes.
- Each node is at most \( k \) positions away from its target position in the sorted list.

Objective:
- Sort the doubly linked list.

#### Strategy

Considering that each node is at most \( k \) positions away from its target position, we can utilize the properties of the insertion sort algorithm, which is efficient for nearly sorted data.

#### Steps to Solve

1. **Initialization**:
    - Start from the head of the doubly linked list.
    - Iterate through the list to sort it using insertion sort logic.

2. **Insertion Sort Algorithm for Doubly Linked List**:
    - For each node, compare it with the previous nodes (up to \( k \) nodes) and find its correct position.
    - Insert the node into its correct position by adjusting the pointers of adjacent nodes.

3. **Implementation**:
    - Traverse the list from the second node to the end.
    - For each node, traverse back up to \( k \) positions to find the correct position.
    - Perform the insertion by adjusting the `prev` and `next` pointers.

#### Code Implementation

Here's the implementation in Python:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertionSortDoublyLinkedList(head, k):
    if head is None:
        return head

    current = head.next
    while current is not None:
        next_node = current.next
        insert_node = current
        # Traverse backwards up to k positions to find the correct position for insert_node
        while insert_node.prev is not None and insert_node.data < insert_node.prev.data:
            # Swap data
            insert_node.data, insert_node.prev.data = insert_node.prev.data, insert_node.data
            insert_node = insert_node.prev
        current = next_node

    return head

def printList(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()

# Helper function to create a doubly linked list from a list of values
def createDoublyLinkedList(arr):
    if not arr:
        return None

    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        new_node = Node(value)
        current.next = new_node
        new_node.prev = current
        current = current.next

    return head

# Example usage:
arr = [3, 6, 2, 12, 56, 8]
k = 2
head = createDoublyLinkedList(arr)
print("Original list:")
printList(head)

head = insertionSortDoublyLinkedList(head, k)
print("Sorted list:")
printList(head)
```

### Complexity Analysis

- **Time Complexity**: The worst-case time complexity of the modified insertion sort for the doubly linked list is \( O(nk) \). In each iteration, we potentially move a node back up to \( k \) positions, leading to a total of \( n \) iterations and \( k \) comparisons/swaps per iteration.
  
- **Space Complexity**: The space complexity is \( O(1) \) as we are not using any extra space except for a few temporary variables for swapping nodes.

This approach efficiently sorts the doubly linked list given the constraint that each node is at most \( k \) positions away from its target position.