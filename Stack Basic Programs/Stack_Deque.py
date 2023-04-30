'''
The collections module contains deque, 
which is useful for creating Python stacks. 
deque stands for "double ended queue"
'''

'''
Why List takes more time than the deque?

List is based on contiguous memory , so whenever , the list wants a new memory
It fetches the free space side of the previous element , if it is not there , 
it fetches another block to make it arrange for that. So, this process , is taking
more time. List is made for optimal slicing and trimming and indexing.

Deque on another hand built upon doubly linked list. 
In a linked list structure, 
Each entry is stored in its own memory block 
and has a reference to the next entry in the list.
A doubly linked list is just the same, 
except that each entry has references to both the previous and the next entry in the list. 
This allows you to easily add nodes to either end of the list.
When we are trying to add a new element , to the queue , 
we basically add a new element at the top of the stack , 
by poininting the previous to the previous top of the stack

On Deque , the major , benifit is , 
constant time addition and removal of entries onto a stack.
So , constant time append() and pop() operations make deque an
excellent choice for implementing a python stack
'''
from collections import deque
myStack = deque()

myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)

myStack.pop()
myStack.pop()
myStack.pop()