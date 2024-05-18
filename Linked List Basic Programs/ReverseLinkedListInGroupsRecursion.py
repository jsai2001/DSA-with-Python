"""
To reverse every k nodes in a linked list, we need to write a function that will perform the following tasks:

Traverse the linked list in chunks of size k.
Reverse the nodes in each chunk.
Connect the reversed chunks appropriately.

This process , will be started from the end of linked list and moves towards start of LL ,
as this follows recursion. First , you will split LL in chunks of size k from start ,
Iterate to the last , and reverse that part of the list and store in new_head node ,
and move furthur , do the same process , until last , at last after reversing all the chunks ,
Join all the new_heads to previous chunks.
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # Helper function to reverse a portion of the linked list
    def reverse_linked_list(start, end):
        prev, curr = None, start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    # Check the length of the linked list is at least k
    count = 0
    node = head
    while node and count < k:
        node = node.next
        count += 1

    if count < k:
        return head  # If the number of nodes is less than k, return head

    # Reverse first k nodes
    new_head = reverse_linked_list(head, node)

    # Recursively call function for the remaining part of the list and attach it to the last node of the reversed list
    head.next = reverseKGroup(node, k)

    return new_head


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
Explanation:

ListNode Class: A basic implementation of a singly linked list node.
reverseKGroup Function: This is the main function that reverses every k nodes in the linked list.
    reverse_linked_list Helper Function: This function reverses a section of the linked list from start to end.
    Checking the List Length: The function first checks if there are at least k nodes left in the list.
    Reversing k Nodes: If there are at least k nodes, it reverses the first k nodes.
    Recursive Call: The function then calls itself recursively to process the rest of the list.
Helper Functions:
    create_linked_list: Converts a Python list into a linked list.
    print_linked_list: Prints the linked list in a readable format.

This implementation ensures that every k-group in the linked list is reversed while the leftover nodes, 
if less than k, are also reversed in the end.

Time Complexity:

The time complexity is indeed O(n). Here’s why:
    The function iterates through each node of the linked list exactly once.
    The main operations (like counting nodes, reversing k nodes, and making recursive calls) all involve traversing parts of the list, but in aggregate, 
each node is processed a constant number of times (specifically, each node is part of exactly one reversal and one counting operation).

Space Complexity

The space complexity of the provided solution is O(n) due to the recursion. Here’s a detailed breakdown:
    Recursive Call Stack: The function makes recursive calls for every segment of k nodes. In the worst case, there could be recursive calls.
    Auxiliary Space for Reversing: The reverse_linked_list function uses a constant amount of space (O(1)) since it uses a few pointers to reverse the nodes.
However, since the recursion depth is proportional to the number of groups of k nodes, the space complexity due to the call stack is 
In the worst case, if k is 1, this becomes O(n).
"""
