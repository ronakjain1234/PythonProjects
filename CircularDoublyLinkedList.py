class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.previous = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break

    # Creation of Circular Doubly Linked List
    def creatCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.previous = newNode
        newNode.next = newNode
        return "The CDLL is created successfully"
    
    # Insertion Method in Circular Doubly Linked List
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist!"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.previous = self.tail
                self.head.previous = newNode
                self.tail.next = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.previous = self.tail
                self.head.previous = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.previous = tempNode
                newNode.next.previous = newNode
                tempNode.next = newNode
            return "The node has been successfully inserted!"
    
    # Traversal of Circular Doubly Linked list
    def traversalCDLL(self):
        if self.head is None:
            print("There is not any node for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
    
    # Reverse Traversal of Circular Doubly Linked List
    def reverseTraversalCDLL(self):
        if self.head is None:
            print("There is not any node for reverse traversal!")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.previous
    
    # Searhing for a given node in a Circular Doubly Linked List
    def searchCDLL(self, value):
        if self.head is None:
            return 'The Circular Doubly Linked List does not exist!'
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == value:
                    return f'{value} exist in the circular doubly linked list!'
                else:
                    tempnode = tempnode.next
                if tempnode == self.tail:
                    return f'{value} does not exist in the circular doubly linked list!'
                
    # Deleting a node from a Circular Doubly Linked List
    def delete_node(self, index):
        if self.head is None:
            return "There is not any element in the Doubly Linked List"
        else: 
            if index == 0:
                if self.head == self.tail:
                    self.head.previous = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.previous = self.tail
                    self.tail.next = self.head
            elif index == -1:
                if self.head == self.tail:
                    self.head.previous = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = self.head
                    self.head.previous = self.tail
            else:
                tempNode = self.head
                temp_Index = 0
                while temp_Index < index - 1:
                    tempNode = tempNode.next
                    temp_Index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.previous = tempNode
        return "Successfully deleted the Node!"
    
    #Deleting the Entire Circular Doubly Linked List
    def deleteCRDLL(self):
        if self.head is None:
            print("There are not any elements to delete!")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode is not None:
                tempNode.previous = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None


    

            



            
    



circularDLL = CircularDoublyLinkedList()
circularDLL.creatCDLL(5)
circularDLL.insertCDLL(1,0)
circularDLL.insertCDLL(3,-1)
circularDLL.insertCDLL(6,2)
circularDLL.insertCDLL(4,1)
print(circularDLL.searchCDLL(100))
print([node.value for node in circularDLL])
circularDLL.deleteCRDLL()
print([node.value for node in circularDLL])

