### Detect and Remove a loop in a Linked List

To solve the problem of detecting and removing a loop in a linked list, we can use Floyd’s Cycle-Finding Algorithm, also known as the Tortoise and Hare algorithm. This method is efficient and can detect a cycle in O(n) time with O(1) space.

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(1)\)

Here’s a step-by-step explanation of the algorithm:

1. **Detecting the Loop**: 
   - Use two pointers, slow and fast. Initially, both pointers point to the head of the list.
   - Move the slow pointer one step at a time and the fast pointer two steps at a time.
   - If there is a loop, the fast pointer will eventually meet the slow pointer within the loop. If there is no loop, the fast pointer will reach the end of the list.

2. **Finding the Start of the Loop**:
   - Once a loop is detected, reset the slow pointer to the head of the list.
   - Move both slow and fast pointers one step at a time. The point at which they meet will be the start of the loop.

3. **Removing the Loop**:
   - To remove the loop, traverse the loop to find the node whose next pointer points to the start of the loop.
   - Set this node’s next pointer to null.

Let's implement this in Python:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def detect_and_remove_loop(head):
    if head is None or head.next is None:
        return

    slow = fast = head
    loop_detected = False

    # Detect loop using Floyd’s Cycle-Finding Algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            loop_detected = True
            break

    # If loop is detected, find the start of the loop
    if loop_detected:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Both slow and fast are now at the start of the loop.
        # To remove the loop, find the node before the start of the loop.
        while fast.next != slow:
            fast = fast.next

        # Remove loop
        fast.next = None

# Helper functions to create and print linked list for testing
def create_linked_list(values, pos):
    head = Node(values[0])
    current = head
    loop_node = None

    for index in range(1, len(values)):
        new_node = Node(values[index])
        current.next = new_node
        current = new_node
        if index == pos - 1:
            loop_node = new_node

    if pos != 0:
        current.next = loop_node

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Test the function
n = 6
values = [1, 2, 3, 4, 5, 6]
pos = 3

head = create_linked_list(values, pos)
print("Linked list before removing loop:")
print_linked_list(head)

detect_and_remove_loop(head)
print("Linked list after removing loop:")
print_linked_list(head)
```

### Explanation

1. **Node Class**:
   - A basic node structure with a value and a next pointer.

2. **detect_and_remove_loop Function**:
   - Uses Floyd’s Cycle-Finding Algorithm to detect a loop.
   - If a loop is detected, it finds the start of the loop.
   - Removes the loop by setting the next pointer of the last node in the loop to None.

3. **Helper Functions**:
   - `create_linked_list`: Creates a linked list from a list of values and links the last node back to a specified position to form a loop.
   - `print_linked_list`: Prints the linked list.

### Time and Space Complexity

- **Time Complexity**: O(n)
  - Detecting the loop: O(n)
  - Finding the start of the loop: O(n)
  - Removing the loop: O(n)
- **Space Complexity**: O(1)
  - Only a few extra pointers are used (slow and fast), so the space complexity is constant.

This approach ensures that the loop, if present, is removed efficiently while maintaining the integrity of the linked list.