"""
Time Complexity:
enqueue: O(1)
dequeue: O(1)
is_empty: O(1)
size: O(1)
peek: O(1)

Space Complexity:
O(n) for storing n elements in the list.
"""
"""
Using a list for a queue is simple, but removing the first element using pop(0) is an O(n) operation since all subsequent elements need to be shifted one position to the left. This is inefficient for large queues.

To address this inefficiency, a deque (double-ended queue) from the collections module can be used. Deque supports O(1) time complexity for append and pop operations from both ends.

Queue Implementation Using Deque:
"""
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("Dequeue from an empty queue")

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from an empty queue")

# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # Output: 1
    print(q.peek())     # Output: 2
    print(q.size())     # Output: 2
"""
Explanation
The implementation is similar to the list-based queue, but it uses a deque:

Initialization: The __init__ method initializes the queue using a deque.
enqueue: Adds an item to the end of the deque.
dequeue: Removes and returns the item from the front of the deque.
All other methods: They work the same as in the list-based implementation but are more efficient.
Using a deque ensures that both enqueue and dequeue operations are performed in constant time, making it suitable for use in performance-sensitive applications.
"""