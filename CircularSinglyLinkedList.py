class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    #Creation of circular singly linked list
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"
    
    # Insertion of a node in a circular singly linked list
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
        return "The node has been successfully inserted"
    
    # Traversing through a circular singly linked list
    def traversalCSLL(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.head:
                    break

    # Searching for a node in a circular singly linked list

    def searchCSLL(self,nodeValue):
        if self.head is None:
            return "There is not any node in this CSLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return f"{nodeValue} does exist in the CSLL"
                tempNode = tempNode.next
                if tempNode == self.head:
                    return f"{nodeValue} does not exist in the CSLL"
                
    # Delete a node from a circular singly linked list
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any noede in CSLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    self.tail = tempNode
                    tempNode.next = self.head
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                currentNode = tempNode.next
                tempNode.next = currentNode.next
    #Delete Entire Circular Singly Linked List
    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None




                


      

    

            

circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(10)
circularSLL.insertCSLL(2,-1)
circularSLL.insertCSLL(1,-1)
circularSLL.insertCSLL(1,-1)
print([node.value for node in circularSLL])
circularSLL.deleteEntireCSLL()


print([node.value for node in circularSLL])

