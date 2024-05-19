"""
Time Complexity:
enqueue: O(1)
dequeue: O(n)
is_empty: O(1)
size: O(1)
peek: O(1)

Space Complexity:
O(n) for storing n elements in the list.
"""
"""
Implementing a queue from scratch in Python can be done using a list 
to hold the elements and managing the insertion (enqueue) and removal (dequeue) operations. 
Here’s how you can implement a basic queue class:

Queue Implementation Using List
"""
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
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
Initialization: The __init__ method initializes the queue using an empty list.
is_empty: Checks if the queue is empty by checking the length of the list.
enqueue: Adds an item to the end of the list.
dequeue: Removes and returns the item from the front of the list. Raises an IndexError if the queue is empty.
size: Returns the number of items in the queue.
peek: Returns the item at the front of the queue without removing it. Raises an IndexError if the queue is empty.
"""