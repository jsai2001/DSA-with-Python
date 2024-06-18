Implementing merge sort for linked lists and provide detailed documentation along with time and space complexity analysis.

### Merge Sort for Linked Lists

Merge Sort is a divide-and-conquer algorithm that works by recursively splitting the list into halves, sorting each half, and then merging the sorted halves back together. For linked lists, this is particularly useful because we can efficiently split and merge without needing extra space for copying elements, unlike arrays.

- **Time Complexity:** \(O(n \log n)\)

- **Space Complexity:** \(O(\log n)\)

### Steps for Merge Sort on Linked Lists

1. **Divide**: Find the middle of the linked list to split it into two halves.
2. **Sort**: Recursively apply merge sort on each half.
3. **Merge**: Merge the two sorted halves back together.

### Implementation Details

#### 1. Find the Middle of the Linked List
To find the middle of the linked list, we can use the "slow and fast pointer" technique. The slow pointer moves one step at a time while the fast pointer moves two steps at a time. When the fast pointer reaches the end, the slow pointer will be at the middle.

#### 2. Merge Two Sorted Linked Lists
To merge two sorted linked lists, we create a dummy node and use a pointer to track the end of the result list. We compare the nodes from both lists one by one and append the smaller node to the result list.

#### 3. Recursive Merge Sort Function
We recursively split the list until we reach the base case where the list is either empty or has only one node (which is inherently sorted).

### Code Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort(head):
    if not head or not head.next:
        return head

    # Step 1: Split the linked list into halves
    mid = get_middle(head)
    next_to_mid = mid.next
    mid.next = None

    # Recursively split & sort
    left = merge_sort(head)
    right = merge_sort(next_to_mid)

    # Step 2: Merge the sorted halves
    sorted_list = sorted_merge(left, right)
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def sorted_merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.val <= right.val:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)

    return result
```

### Explanation

1. **ListNode Class**: Defines a node in the linked list.
2. **merge_sort Function**:
    - Base case: If the list is empty or has only one node, it is already sorted.
    - Split the list into two halves using `get_middle`.
    - Recursively sort both halves.
    - Merge the two sorted halves using `sorted_merge`.
3. **get_middle Function**: Uses the slow and fast pointer approach to find the middle of the linked list.
4. **sorted_merge Function**: Merges two sorted linked lists into one.

### Time and Space Complexity

#### Time Complexity
- **Splitting the List**: Finding the middle of the list takes \(O(n)\).
- **Merging**: Merging two sorted lists takes \(O(n)\).
- Since each level of recursion splits the list into two halves, and merging those halves takes linear time, the overall time complexity is \(O(n \log n)\).

#### Space Complexity
- The space complexity is \(O(\log n)\) due to the recursive stack used for splitting the list. There is no additional space needed for merging the lists.

In summary, the merge sort algorithm for linked lists efficiently sorts the list in \(O(n \log n)\) time with \(O(\log n)\) space complexity due to recursion. This implementation leverages the inherent properties of linked lists for optimal performance.