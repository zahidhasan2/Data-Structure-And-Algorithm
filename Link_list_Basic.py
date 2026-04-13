
# linked_list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# print(node1.data)
# print(node1.next)

node1.next=node2
node2.next=node3
node3.next=node4

print(node1)
print(node1.next.next.data)




