### Intersection Point in Y Shaped Linked Lists

Let's solve the problem of finding the intersection point of two singly linked lists. The problem can be approached in multiple ways, but I'll describe an efficient method using two-pointer technique.

### Problem Explanation
Given two singly linked lists, the goal is to find the node at which the two linked lists intersect. Intersecting means that from this node onwards, the nodes are shared between the two lists.

- **Time Complexity:** \(O(N + M)\)

- **Space Complexity:** \(O(1)\)

### Approach
We can solve this problem using the following steps:

1. **Calculate the Length of Both Lists:**
   - Traverse each list to find its length.
2. **Align the Start of Both Lists:**
   - If one list is longer than the other, advance the pointer in the longer list by the difference in lengths.
3. **Traverse and Compare:**
   - Traverse both lists simultaneously and compare the nodes. The first common node is the intersection point.

### Detailed Steps
1. **Calculate Length:**
   - Traverse through List1 to calculate its length.
   - Traverse through List2 to calculate its length.

2. **Align the Start:**
   - Calculate the difference in lengths of the two lists.
   - Move the pointer in the longer list ahead by the difference in lengths.

3. **Traverse and Compare:**
   - Move both pointers one step at a time in both lists.
   - Check if the nodes are the same. If they are, that is the intersection point.

### Example
Consider the following linked lists:
- List1: 1 -> 2 -> 3 -> 4 -> 5 -> 6
- List2: 9 -> 5 -> 6 (intersection starts at node with value 5)

### Implementation
Here's a Python implementation of the approach:

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def get_intersection_node(head1, head2):
    # Calculate lengths of both lists
    len1 = get_length(head1)
    len2 = get_length(head2)
    
    # Calculate the difference in lengths
    if len1 > len2:
        for _ in range(len1 - len2):
            head1 = head1.next
    else:
        for _ in range(len2 - len1):
            head2 = head2.next
    
    # Move both pointers and check for intersection
    while head1 and head2:
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next
    
    # If no intersection
    return None

# Helper function to print the list from a given node
def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Example usage:
# Creating the intersection list: 5 -> 6
intersect = ListNode(5, ListNode(6))

# List1: 1 -> 2 -> 3 -> 4 -> intersect
list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, intersect))))

# List2: 9 -> intersect
list2 = ListNode(9, intersect)

# Print lists
print("List1: ", end="")
print_list(list1)
print("List2: ", end="")
print_list(list2)

# Get intersection node
intersection_node = get_intersection_node(list1, list2)
if intersection_node:
    print(f"The intersection point is at node with value: {intersection_node.value}")
else:
    print("No intersection point found.")
```

### Time and Space Complexity
- **Time Complexity:** O(N + M)
  - Calculating the lengths of the lists takes O(N) and O(M).
  - Aligning the pointers takes O(N - M) steps, which is at most O(N) or O(M).
  - Traversing the lists to find the intersection takes O(min(N, M)) steps.
  - Overall, this results in O(N + M) time complexity.
  
- **Space Complexity:** O(1)
  - We are using a constant amount of extra space, regardless of the input size.

This approach is efficient and ensures that we find the intersection point, if it exists, with minimal overhead.