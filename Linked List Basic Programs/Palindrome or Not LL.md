### Linked List is a Palindrome or not

To determine whether a singly linked list is a palindrome, we can follow these steps:

- **Time Complexity:** \(O(N)\)

- **Space Complexity:** \(O(1)\)

1. **Find the middle of the linked list**: This can be done using the slow and fast pointer technique.
2. **Reverse the second half of the linked list**: Once we find the middle, we reverse the second half of the list.
3. **Compare the first half and the reversed second half**: Finally, we compare the nodes from the beginning and from the middle (reversed) to check if they are the same.

Here's a Python program to achieve this:

### Detailed Explanation and Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    """
    This function checks whether a singly linked list is a palindrome.
    
    Parameters:
    head (ListNode): The head node of the singly linked list.
    
    Returns:
    bool: True if the linked list is a palindrome, False otherwise.
    """
    
    # Edge case: An empty list or a list with a single node is a palindrome
    if not head or not head.next:
        return True

    # Step 1: Find the middle of the linked list using slow and fast pointers
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half of the linked list
    prev = None
    curr = slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    # Step 3: Compare the first half and the reversed second half
    first_half, second_half = head, prev
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

# Helper function to create a linked list from a list
def create_linked_list(lst):
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example Usage
lst = [1, 2, 2, 1]
head = create_linked_list(lst)
print(isPalindrome(head))  # Output: True

lst = [1, 2, 3, 2, 1]
head = create_linked_list(lst)
print(isPalindrome(head))  # Output: True

lst = [1, 2]
head = create_linked_list(lst)
print(isPalindrome(head))  # Output: False
```

### Explanation

1. **Finding the Middle**:
   - We use two pointers, `slow` and `fast`. `slow` moves one step at a time, while `fast` moves two steps at a time. By the time `fast` reaches the end of the list, `slow` will be at the middle.
   
2. **Reversing the Second Half**:
   - Starting from the middle, we reverse the second half of the list. This involves iterating through the second half and reversing the links between nodes.
   
3. **Comparing Both Halves**:
   - Finally, we compare the nodes in the first half with the nodes in the reversed second half. If all corresponding nodes are equal, the list is a palindrome.

### Time Complexity

- Finding the middle: O(n)
- Reversing the second half: O(n)
- Comparing the two halves: O(n)

Overall, the time complexity is O(n), where n is the number of nodes in the linked list.

### Space Complexity

- The space complexity is O(1) since we are using a constant amount of extra space regardless of the input size.