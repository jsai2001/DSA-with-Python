#Stack operation using List
myStack = []
#Push an element into the list
myStack.append('a')
myStack.append('b')
myStack.append('c')
#Display all elements of the list
print(myStack)
#Pop an element from the stack
myStack.pop()
print("Status of the array: ",myStack)
myStack.pop()
print("Status of the array: ",myStack)
myStack.pop()
print("Status of the array: ",myStack)

#We get an IndexError in here because , the list / Stack is empty
myStack.pop()

'''
Lists are defined , for faster access to random elements in the list , 
It means the items are stored next to each other in the memory

Lists with more number of elements , makes the operations slower and sluggier.
When the size of the list is large , append() function takes longer time , 
insert() function takes much more longer time.
'''
