class Node:
    def __init__(self,data):
        '''
        This is the structure of the Node
        * data variable contains the Node's data
        * next variable contains the Address of the next node
        '''
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        '''
        For a stack , we are initializing two variables in global
        * top variable , which contains the address of top node
        * stackSize variable consists of size of the stack
        '''
        self.top = None
        self.stackSize = 0
    def push(self,data):
        '''
        Create a Node , with data , may be the next would be None
        
        If the stack is empty , add one element into the stack
        Else add one element upon the existing top element
        '''
        temp = Node(data)
        if self.top is None:
            self.top = temp
            self.stackSize+=1
        else:
            temp.next = self.top
            self.top = temp
            self.stackSize+=1
    def pop(self):
        '''
        If there is no top element in the stack then 
        raise and "Stack is Empty" exception
        Else move top pointer one step below , so we can 
        escape the top and decrease the stack size by 1
        And remove the space occupied by the stop pointer
        '''
        try:
            if self.top == None:
                raise Exception("Stack is Empty")
            else:
                temp = self.top
                self.top = self.top.next
                tempdata = temp.data
                self.stackSize-=1
                del temp
                return tempdata
        except Exception as e:
            print(str(e))
    def isEmpty(self):
        '''
        If stackSize is 0 , then return true as it is empty
        Else return false as it isn't empty
        '''
        if self.stackSize==0:
            return True
        else:
            return False
    def size(self):
        '''Return size of the stack'''
        return self.stackSize
    def top_element(self):
        '''
        If top element is not yet assigned , then stack isn't empty
        Else return the top most node's data
        '''
        try:
            if self.top == None:
                raise Exception("Stack is Empty")
            else:
                return self.top.data
        except Exception as e:
            print(str(e))

s = Stack()
s.push(1)
print("Stage 1: ",s.size())

s.push(2)
print("Stage 2: ",s.size())

print(s.pop())
print("Stage 3: ",s.size())

print(s.pop())
print("Stage 4: ",s.stackSize)

print("Top element of the Stack: ",s.top_element())
print("List Empty or Not: ",s.isEmpty())