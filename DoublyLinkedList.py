class Node:
    def __init__ (self, value = None):
        self.value = value
        self.next = None
        self.previous = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # Creation of Doubly Linked list
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = None
        node.previous = None
        self.head = node
        self.tail = node
        return "The DLL is created Successfully"
    
    #Inserting an element in a Doubly Linked List
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.previous = None
                newNode.next = self.head
                self.head.previous = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.previous = self.tail
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
    # Traversing through a doubly linked list
    def traverse(self):
        if self.head is None:
            print("There is not any element to traverse.")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    # Reverse Traversal Method in Doubly Linked List
    def ReverseTraversalDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.previous
    
    # Search Method in Doubly Linked List
    def search(self, nodeValue):
        if self.head is None:
            return "There is not any element in the list."
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return f"{nodeValue} does exist in the linked list!"
                tempNode = tempNode.next
            return f"{nodeValue} does not exist in the linked list!"
    
    # Delete a node from Doubly Linked list
    def deleteNode(self,location):
        if self.head is None:
            print("There is not any element in the Doubly Linked List!")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else: 
                    self.head = self.head.next
                    self.head.previous = None
            elif location ==-1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.previous = tempNode
            print("The node has been successfully added!")

    #Delete entire Doubly Linked List
    def deleteDLL(self):
        if self.head is None:
            print("There is not any Node in the DLL!")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.previous = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted!")

                 

    

doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)
doublyLL.insertNode(1,0)
doublyLL.insertNode(3,-1)
doublyLL.insertNode(4,-1)
doublyLL.insertNode(10,2)

print([node.value for node in doublyLL])

doublyLL.deleteDLL()
print([node.value for node in doublyLL])

