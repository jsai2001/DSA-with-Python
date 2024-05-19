"""
Time Complexity:
    Push: O(1)
    Pop: O(1)
    Peek: O(1)
    Is Empty: O(1)
    Size: O(1)

Space Complexity:
    Overall: O(n)
"""
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.items = []

    def is_empty(self):
        # Return True if the stack is empty, False otherwise
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item from the stack
        # Raise an error if the stack is empty
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        # Return the top item from the stack without removing it
        # Raise an error if the stack is empty
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

    def __str__(self):
        # Return a string representation of the stack
        return str(self.items)

# Example usage:
if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack after pushes:", stack)
    print("Top element:", stack.peek())
    print("Stack size:", stack.size())

    print("Popped element:", stack.pop())
    print("Stack after pop:", stack)

    print("Is stack empty?", stack.is_empty())
    stack.pop()
    stack.pop()
    print("Is stack empty after popping all elements?", stack.is_empty())
"""
Explanation:

Initialization (__init__ method):

The __init__ method initializes an empty list self.items to store the elements of the stack.
Check if the Stack is Empty (is_empty method):

The is_empty method returns True if the stack is empty (i.e., self.items has no elements), otherwise it returns False.
Push Operation (push method):

The push method appends the given item to the end of the list self.items.
Pop Operation (pop method):

The pop method removes and returns the last item from self.items. If the stack is empty, it raises an IndexError.
Peek Operation (peek method):

The peek method returns the last item from self.items without removing it. If the stack is empty, it raises an IndexError.
Size of the Stack (size method):

The size method returns the number of elements in the stack.
String Representation (__str__ method):

The __str__ method returns a string representation of the stack, which helps in printing the stack's content.

Time Complexity:
    Push: O(1)
    Pop: O(1)
    Peek: O(1)
    Is Empty: O(1)
    Size: O(1)

Space Complexity:
    Overall: O(n) for storing n elements in the stack. The auxiliary space is O(1).

is_empty and size operation occupy O(1) , irrespective of having len() function under it ,
Python lists are implemented as dynamic arrays. 
The length of the list is maintained as an attribute of the list object, 
so retrieving this length is a simple attribute access, which is O(1).
"""
