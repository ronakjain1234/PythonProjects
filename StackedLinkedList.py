class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        value = [str(x.value) for x in self.LinkedList]
        return'\n'.join(value)
        
    #Checks if the stack is empty
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    # Adds an element to the stack
    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    # Deletes the first element in the Linked List
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack!"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    # Returns the fist element in the stack
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack!"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
    
    # Deletes the entire stack
    def delete(self):
        self.LinkedList.head = None
    
    
        
customStack = Stack()
customStack.push(3)
customStack.push(2)
customStack.push(1)
 

