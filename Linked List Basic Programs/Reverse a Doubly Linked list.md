Reversing a doubly linked list involves reversing the direction of the pointers (previous and next) for each node in the list. Here's a detailed explanation, along with the implementation and analysis of time and space complexity.

### Detailed Explanation

A doubly linked list is a type of linked list where each node contains three fields: a data field, a pointer to the next node in the sequence, and a pointer to the previous node. Reversing this list means that for each node, we need to swap its `next` and `prev` pointers.

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(1)\)

### Steps to Reverse a Doubly Linked List

1. **Initialization**: 
    - Start with the head of the list.
    - Use a temporary pointer to help with the reversal process.

2. **Traversal and Reversal**:
    - For each node, swap its `next` and `prev` pointers.
    - Move to the next node in the original list, which is now the previous node after swapping.
    - Keep track of the previous node to update the head of the reversed list at the end.

3. **Update the Head**:
    - Once all nodes are processed, update the head to be the last node processed.

### Implementation in Python

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def reverse(self):
        current = self.head
        temp = None
        while current:
            # Swap the next and prev pointers
            temp = current.prev
            current.prev = current.next
            current.next = temp
            # Move to the next node in the original list
            current = current.prev
        if temp:
            self.head = temp.prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

print("Original List:")
dll.display()

dll.reverse()

print("Reversed List:")
dll.display()
```

### Time Complexity

- **Traversal**: We traverse the entire list once, which takes \(O(n)\) time where \(n\) is the number of nodes in the list.
- **Reversal**: The reversal operation involves swapping pointers, which is \(O(1)\) for each node. Since we do this for all \(n\) nodes, the total time complexity remains \(O(n)\).

### Space Complexity

- The space complexity is \(O(1)\) because we only use a few extra variables (`current` and `temp`) regardless of the size of the input list. The space required does not scale with the input size.

### Conclusion

Reversing a doubly linked list is an efficient operation with linear time complexity and constant space complexity. This makes it suitable for applications where in-place modification of the list is required. The provided implementation swaps the pointers of each node, effectively reversing the list while maintaining the integrity of the data structure.