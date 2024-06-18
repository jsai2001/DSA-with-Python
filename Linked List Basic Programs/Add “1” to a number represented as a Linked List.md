### Add “1” to a number represented as a Linked List

To solve the problem of adding 1 to a number represented by a linked list, we need to simulate the process of addition starting from the least significant digit (which is typically the last node in the list) and propagate any carry towards the most significant digit (the head of the list).

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(1)\)

Here is a step-by-step explanation and the corresponding code:

### Steps to Add 1 to a Number Represented by a Linked List

1. **Reverse the Linked List**:
    - Start by reversing the linked list to facilitate easy addition from the least significant digit.
  
2. **Add 1 to the Number**:
    - Initialize carry as 1 (since we need to add 1).
    - Traverse the reversed list, add the carry to the current node's value, update the node's value, and determine the new carry.
    - If carry becomes 0, stop the addition process as there’s no further propagation needed.

3. **Reverse the List Again**:
    - Reverse the list again to restore the original order but with the updated number.

4. **Handle Remaining Carry**:
    - If after processing all nodes the carry is still 1, it means we need an extra node to handle the overflow (e.g., adding 1 to 999 results in 1000).

### Detailed Documentation

#### Data Structure Definitions
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

#### Helper Functions
- **Reverse the Linked List**:
```python
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```

- **Add 1 to the Reversed List**:
```python
def add_one_to_list(head):
    current = head
    carry = 1
    while current:
        new_value = current.val + carry
        current.val = new_value % 10
        carry = new_value // 10
        if carry == 0:
            break
        if current.next is None and carry > 0:
            current.next = ListNode(carry)
            break
        current = current.next
    return head
```

- **Main Function to Add 1**:
```python
def add_one_to_linked_list(head):
    if not head:
        return ListNode(1)
    
    # Step 1: Reverse the linked list
    head = reverse_linked_list(head)
    
    # Step 2: Add one to the reversed list
    head = add_one_to_list(head)
    
    # Step 3: Reverse the list again to restore original order
    head = reverse_linked_list(head)
    
    return head
```

### Time and Space Complexity

- **Time Complexity**:
    - Reversing the list takes \(O(n)\) time where \(n\) is the number of nodes.
    - Adding one to the reversed list takes \(O(n)\) in the worst case (when carry propagates through all nodes).
    - Reversing the list again takes \(O(n)\) time.
    - Overall, the time complexity is \(O(n)\).

- **Space Complexity**:
    - The algorithm uses constant extra space, i.e., \(O(1)\), apart from the space required for the input linked list.

### Complete Code
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def add_one_to_list(head):
    current = head
    carry = 1
    while current:
        new_value = current.val + carry
        current.val = new_value % 10
        carry = new_value // 10
        if carry == 0:
            break
        if current.next is None and carry > 0:
            current.next = ListNode(carry)
            break
        current = current.next
    return head

def add_one_to_linked_list(head):
    if not head:
        return ListNode(1)
    
    # Step 1: Reverse the linked list
    head = reverse_linked_list(head)
    
    # Step 2: Add one to the reversed list
    head = add_one_to_list(head)
    
    # Step 3: Reverse the list again to restore original order
    head = reverse_linked_list(head)
    
    return head
```

This solution ensures that the addition of 1 is efficiently handled with optimal time and space complexity.