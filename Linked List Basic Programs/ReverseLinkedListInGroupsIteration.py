"""
Time Complexity:
Space Complexity:
"""
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    def reverse_linked_list(start, end):
        prev, curr = None, start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    
    while True:
        # Check the length of the remaining list
        kth = prev_group_end
        count = 0
        while count < k and kth.next:
            kth = kth.next
            count += 1
        
        if count < k:
            break
        
        group_start = prev_group_end.next
        next_group_start = kth.next
        kth.next = None
        
        # Reverse this k-group
        prev_group_end.next = reverse_linked_list(group_start, None)
        
        group_start.next = next_group_start
        prev_group_end = group_start
    
    return dummy.next

# Helper function to create a linked list from a list and return the head
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(" -> ".join(map(str, values)))


# Example usage:
# Creating a linked list with values from 1 to 8
linked_list = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
k = 3

# Reversing every k group in the linked list
reversed_list = reverseKGroup(linked_list, k)

# Printing the reversed linked list
print_linked_list(reversed_list)
"""
Explanation of Iterative Approach:
Dummy Node: A dummy node is used to simplify edge cases such as reversing the first k nodes.
Traversal to Find kth Node: A loop counts k nodes ahead to ensure there are enough nodes to reverse. If fewer than k nodes remain, the process terminates.
Reverse k Nodes: The reverse_linked_list helper function reverses the k nodes.
Reconnect the Segments: After reversing, the segments are reconnected properly.
By using this iterative approach, the space complexity is reduced to O(1) since the recursion stack is eliminated, and only a constant amount of extra space is used.

Detailed Explanation

Initialization:
    A dummy node (dummy) is created and linked to the head of the list. This dummy node helps manage edge cases, such as reversing the first k nodes.
    prev_group_end is initialized to the dummy node. This pointer keeps track of the end of the previously processed group of nodes.

Outer While Loop:
    The outer while True loop continues to process the list in chunks of k nodes until there are fewer than k nodes left.

Finding the kth Node:
    kth is initialized to prev_group_end. This pointer is used to find the end of the current group of k nodes.
    The inner while loop increments kth k times, ensuring there are at least k nodes available for reversal.
    If the inner loop completes without finding k nodes (count < k), the list's remaining nodes are fewer than k and should not be reversed. Hence, the loop breaks.

Setting up for Reversal:
    group_start is set to prev_group_end.next, marking the start of the current group to be reversed.
    next_group_start is set to kth.next, which is the node right after the current group. This helps reconnect the reversed group to the rest of the list after reversal.
    kth.next is set to None to temporarily disconnect the current group from the rest of the list, making it easier to reverse.

Reversing the Current k-group:
    reverse_linked_list(group_start, None) reverses the current k-group of nodes.
    prev_group_end.next is updated to point to the new head of the reversed group.

Reconnecting and Moving to the Next Group:
    group_start.next (which was the start of the current group and is now the end after reversal) is set to next_group_start, reconnecting the reversed group to the next part of the list.
    prev_group_end is updated to group_start, which is now the end of the reversed group. This sets up the pointer for the next iteration.
"""
# Example Walkthrough
"""
Let's go through an example step-by-step. Assume the linked list is 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 and k=3:

First Group:
    kth moves 3 steps: 1 -> 2 -> 3
    next_group_start is 4
    Reverse 1 -> 2 -> 3 to 3 -> 2 -> 1
    Connect 3 -> 2 -> 1 -> 4
    Move prev_group_end to 1
Second Group:
    kth moves 3 steps: 4 -> 5 -> 6
    next_group_start is 7
    Reverse 4 -> 5 -> 6 to 6 -> 5 -> 4
    Connect 1 -> 6 -> 5 -> 4 -> 7
    Move prev_group_end to 4
Third Group:
    kth moves 3 steps: 7 -> 8
    Only 2 nodes left, so break the loop without reversing.
Final list: 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 7 -> 8.

This approach ensures the linked list is processed in groups of k nodes, 
reversing each group and connecting them properly, with space complexity of O(1).
"""
