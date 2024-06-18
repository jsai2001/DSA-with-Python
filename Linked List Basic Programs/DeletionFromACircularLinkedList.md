### Deletion from a Circular Linked List

Deletion from a circular linked list involves removing a specified node from the list. In a circular linked list, the last node points back to the head, forming a circle. Here's a detailed explanation and Python implementation for deleting a node from a circular linked list.

### Detailed Explanation

#### Steps for Deletion

1. **Identify the Node to be Deleted**:
   - If the node to be deleted is the head node.
   - If the node to be deleted is any other node.

2. **Adjust Pointers**:
   - For the head node: Adjust the last node's next pointer to point to the new head.
   - For any other node: Adjust the previous node's next pointer to skip the node to be deleted and point to the node after it.

3. **Handle Special Cases**:
   - If the list is empty.
   - If the list contains only one node.
   - If the node to be deleted is not found.

### Code Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        if not self.head:
            return "List is empty"
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    def delete_node(self, key):
        if self.head is None:
            return "List is empty"

        # If the node to be deleted is the head node
        if self.head.data == key:
            # Only one node in the list
            if self.head.next == self.head:
                self.head = None
                return

            # More than one node in the list
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = self.head.next
            self.head = self.head.next
            return

        # If the node to be deleted is not the head node
        current = self.head
        previous = None
        while current.next != self.head:
            if current.data == key:
                break
            previous = current
            current = current.next

        if current.data == key:
            previous.next = current.next
        else:
            print(f"Node with data {key} not found.")

# Example Usage
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)

print("Original List:")
cll.print_list()

print("\nDeleting node with data 3:")
cll.delete_node(3)
cll.print_list()

print("\nDeleting node with data 1 (head node):")
cll.delete_node(1)
cll.print_list()

print("\nDeleting node with data 5 (non-existent):")
cll.delete_node(5)
cll.print_list()
```

### Time and Space Complexity

**Time Complexity**:
- **O(n)**: In the worst-case scenario, we may need to traverse the entire list to find and delete the node. Here, \( n \) is the number of nodes in the circular linked list.

**Space Complexity**:
- **O(1)**: The space complexity is constant because we only use a few extra variables for traversal and deletion (current, previous, and last).

### Summary

- **Identify the node to be deleted** by traversing the list.
- **Adjust pointers** to bypass the node to be deleted.
- **Handle edge cases** like empty list, single-node list, and node not found.
- The implementation ensures that the list maintains its circular structure after deletion.