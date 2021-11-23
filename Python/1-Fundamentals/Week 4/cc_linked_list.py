class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")

def iter_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next

head.next.next.next = Node("4th Node")
print(head.next.next.next.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:",self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Append new Node with value:",node.next.value)

    def prepend(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:",self.head.value)
            return
        
        new_node = self.head
        while new_node is not None:
            new_node = self.head
            print("")




llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")
