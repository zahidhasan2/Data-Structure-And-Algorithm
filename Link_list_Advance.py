
# linked_list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traversal(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" → ")
                current = current.next
            print("None")
            
    def insert_at(self, val, position):
        new_node = Node(val)

        # Case 1: Insert at head (position = 0)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Case 2: Insert at given position
        current = self.head
        prev_node = None
        count = 0

        while current is not None and count < position:
            prev_node = current
            current = current.next
            count += 1

        # Insert the new node
        prev_node.next = new_node
        new_node.next = current
        
    def delete(self, val):
        temp = self.head
        if temp.next is not None:
            if temp.data == val:   
                self.head = temp.next
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.data == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next

                if found:
                    prev.next = temp.next
                    return
                else:
                    print("Node not found")

        

ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

ll.traversal()
ll.insert_at(20,3)







