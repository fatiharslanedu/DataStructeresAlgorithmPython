class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        pass
    pass

class CircularList():
    def __init__(self):
        self.head = None
        pass
    
    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            cur = self.head
            new_node = Node(data)
            while cur.next is not self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
            self.head = new_node
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:   
            cur_node = self.head
            new_node = Node(data)
            while cur_node.next is not self.head:
                cur_node = cur_node.next
                pass
            cur_node.next = new_node
            new_node.next = self.head
            pass
        pass

    def print_list(self):
        cur_node = self.head
        print("List:", end=' ')
        while cur_node:
            print(cur_node.data, end=' ')
            cur_node = cur_node.next
            if cur_node is self.head:
                break
            pass
        print()
            

l1 = CircularList()
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.prepend(1)
l1.print_list()
            