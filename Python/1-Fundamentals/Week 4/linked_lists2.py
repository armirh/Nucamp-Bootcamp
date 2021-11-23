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
