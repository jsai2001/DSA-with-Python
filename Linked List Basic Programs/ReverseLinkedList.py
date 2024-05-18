"""
Iterative Approach:

Time Complexity: 𝑂(𝑛)
Space Complexity: 𝑂(1)

Recursive Approach:

Time Complexity: O(n)
Space Complexity: O(n)

Recursive Approach

Time Complexity
The recursive approach also involves traversing the entire linked list, 
making a recursive call for each node. Similar to the iterative approach, 
each node is processed once. Hence, the time complexity is O(n).

Space Complexity
In the recursive approach, each recursive call adds a new frame to the call stack. 
For a linked list with n nodes, there will be n recursive calls, each consuming stack space. 
Thus, the space complexity due to the call stack is O(n).
"""
"""
Reversing a linked list can be done using both iterative and recursive approaches. Below are the implementations for each.
"""
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
"""
Iterative approach involves modifying the next pointers of the nodes one by one until all the nodes have been reversed.
"""
def reverse_linked_list_iterative(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev and current one step forward
        current = next_node
    return prev  # New head of the reversed list
"""
Recursive approach reverses the list by solving the problem for the rest of the list and then fixing the current node.
"""
def reverse_linked_list_recursive(head):
    if head is None or head.next is None:
        return head  # Base case: the list is empty or has only one node   
    # Reverse the rest list
    new_head = reverse_linked_list_recursive(head.next)  
    # Fix the current node
    head.next.next = head
    head.next = None  
    return new_head  # New head of the reversed list

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

def create_linked_list_from_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Test the iterative approach
head = create_linked_list_from_list([1, 2, 3, 4, 5])
print("Original linked list:")
print_linked_list(head)

reversed_head_iterative = reverse_linked_list_iterative(head)
print("Reversed linked list (iterative):")
print_linked_list(reversed_head_iterative)

# Since the list is now reversed, we need to recreate it to test the recursive approach
head = create_linked_list_from_list([1, 2, 3, 4, 5])
reversed_head_recursive = reverse_linked_list_recursive(head)
print("Reversed linked list (recursive):")
print_linked_list(reversed_head_recursive)

"""
Iterative Approach: Uses a loop to reverse the pointers of the nodes iteratively.
Recursive Approach: Recursively reverses the rest of the list and then fixes the current node's pointer.
"""
"""
Recursive approch discussion:

new_head = reverse_linked_list_recursive(head.next)
This line calls the reverse_linked_list_recursive function on the next node (head.next).
The function continues calling itself until it reaches the base case: 
if head is None or head.next is None, which stops the recursion. 
This is when it finds the last node of the original list or when the list is empty.
As the recursion unwinds, 
each call returns the new head of the reversed sublist. 
For example, if the list was 1 -> 2 -> 3 -> 4 -> 5, the base case would return 5 as the new head. 
Then, the previous call with head = 4 gets this 5 as new_head, and so on.
"""