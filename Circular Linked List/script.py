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
    
    def remove(self, key):
        cur = self.head
        q = self.head
        prev = None
        if not self.head:
            return
        
        while q.next != self.head:
            q = q.next
        
        if self.head.next == self.head:
            self.head = None
            return
        
        if cur.data == key:
            q.next = cur.next
            self.head = cur.next
            cur = None
            return
        else:
            while cur.next != self.head:
                if cur.data == key:
                    break
                prev = cur
                cur = cur.next
            
            if cur is self.head:
                self.head = None
            
            prev.next = cur.next
            cur = None
        
    def __len__(self):
        cur = self.head
        count = 0
        while cur.next is not self.head:
            count += 1
            cur = cur.next
        return count + 1
            
    def split_list(self):
        size = len(self)
        if size == 0:
            return
        if size == 1:
            return self.head
        
        mid = size // 2
        cur_node = self.head
        prev = None
        count = 0
        while cur_node and count < mid:
            count += 1
            prev = cur_node
            cur_node = cur_node.next
        
        prev.next = self.head
        
        split_cllist = CircularList()
        
        while cur_node.next != self.head:
            split_cllist.append(cur_node.data)
            cur_node = cur_node.next
        split_cllist.append(cur_node.data)
        
        self.print_list()
        print("\n")
        split_cllist.print_list()
        
            
        
        
        
        
        
                  

l1 = CircularList()
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.prepend(1)
l1.print_list()
print("Remove operation")
l1.remove(5)
l1.print_list()
print("Len of string:", len(l1))
l1.split_list()