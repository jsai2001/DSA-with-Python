### Remove Duplicates from a Sorted Linked List

To solve the problem of removing duplicates from a sorted singly linked list without using extra space, we can leverage the fact that the list is already sorted. This means that any duplicates will be adjacent to each other. We can traverse the list and compare each node with the next node, removing any duplicates we find.

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(1)\)

Here is a step-by-step explanation of the solution:

### Steps to Remove Duplicates

1. **Initialize Pointers**:
   - Start with a pointer `current` pointing to the head of the list.

2. **Traverse the List**:
   - While `current` is not `None` and `current.next` is not `None`:
     - Compare `current` node's value with `current.next` node's value.
     - If they are the same, remove the `current.next` node by adjusting the `next` pointer of the `current` node.
     - If they are not the same, move the `current` pointer to the next node.

3. **Update Links**:
   - If duplicates are found, update the links to bypass the duplicate nodes.

### Pseudocode

Here's the pseudocode for the above steps:

```
function removeDuplicates(head):
    if head is None:
        return None
    
    current = head
    
    while current is not None and current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    
    return head
```

### Time Complexity

- The time complexity of this solution is \(O(N)\), where \(N\) is the number of nodes in the linked list. This is because we traverse the list once, making a constant-time comparison and link update for each node.

### Space Complexity

- The space complexity is \(O(1)\) because we are not using any extra space apart from a few pointers for traversal.

### Python Implementation

Below is the Python implementation of the above logic:

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_duplicates(head):
    if head is None:
        return None
    
    current = head
    
    while current is not None and current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

# Helper function to print the linked list
def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

# Example usage
# Creating a sorted linked list with duplicates: 1 -> 1 -> 2 -> 3 -> 3 -> None
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
print("Original list:")
print_list(head)

# Removing duplicates
head = remove_duplicates(head)
print("List after removing duplicates:")
print_list(head)
```

### Explanation of the Example

1. **Original List**: 
   - 1 -> 1 -> 2 -> 3 -> 3 -> None
   
2. **After Removing Duplicates**:
   - We compare the first two nodes (both 1), remove the second one.
   - Compare 1 and 2, move to the next node.
   - Compare 2 and 3, move to the next node.
   - Compare the last two nodes (both 3), remove the second one.
   - Resulting list: 1 -> 2 -> 3 -> None

This implementation ensures that we traverse the list in linear time, adjusting pointers in place without using extra memory.