'''
The deque package which is under collections , is not totally thread safe
Mainly the append and pop operations are thread safe , but when coming to 
other options of deque , they are not thread safe , only append and pop operations runs in a single thread.
rest of the operations are not that secure , so for that case , we are using
lifoQueue() function , which is fully thread safe. In which , indexing and such 
operations are not necessary.
'''

from queue import LifoQueue
myStack = LifoQueue()
#Appending elements on the stack
myStack.put('a')
myStack.put('b')
myStack.put('c')
print("Returns an LifoQueue object: ",myStack)
'''
myStack.get() function returns top element from the stack
If there are no elements in the stack and if we are using the same
get() then , it continously waits for the output, if we don't want
that , we need to use the myStack.get_nowait() function , which 
returns the top element of the stack , if there isn't one , we return 
an Exception
'''
print(myStack.get_nowait())
print(myStack.get_nowait())
print(myStack.get_nowait())
print(myStack.get_nowait())
#We get the following error
'''
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/usr/lib/python3.7/queue.py", line 198, in get_nowait
    return self.get(block=False)
  File "/usr/lib/python3.7/queue.py", line 167, in get
    raise Empty
_queue.Empty
'''
'''
Unlike deque, LifoQueue is designed to be fully thread-safe. 
All of its methods are safe to use in a threaded environment. 
It also adds optional time-outs to its operations which can frequently be a must-have feature in threaded programs.
To make it thread-safe , it typically takes some extra time for each operation,
So , if we see the stack operations are taking a bit more time , and our thread safety,
is not a priority , then we can use deque instead. But when thread safety comes into picture
LifoQueue pops up.

Lists , must be familier to us , but , there are many memory allocation and reallocation issues , 
coming with Lists , So , we have moved to the deque() , deque will be alright , until , there is no 
thread safetly issues are calculated , else , we need to use LifoQueue() , which is threadsafe.
'''
