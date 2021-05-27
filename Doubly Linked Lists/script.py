class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node #todo: fix the none type first
            new_node.prev = cur #todo: assign the previous one
        
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    
    def print_list(self):
        print("List:", end = " ")
        cur = self.head
        while cur:
            print(cur.data, end = " ")
            cur = cur.next
        print()
        
    def add_after_node(self, key, data):
        cur = self.head
        
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next 
                cur.next = new_node
                new_node.prev = cur
                new_node.next = nxt
                nxt.prev = new_node
                return
            cur = cur.next    
      
    def add_before_node(self, key, data):
        cur = self.head
        prev_node = None
        while cur:
            if self.head.data == key:
                self.prepend(data)
                return  
            elif cur.data == key:
                new_node = Node(data)
                nxt = prev_node.next
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = nxt
                nxt.prev = new_node
                return
            prev_node = cur
            cur = cur.next  

    def delete(self, key):
        cur = self.head
        prev_node = None
        while cur:           
            if cur.data == key and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur.prev = None
                    cur.next = None
                    cur = None
                    self.head = None
                    return
                else:
                    # Case 2:
                    self.head = cur.next
                    cur.prev = None
                    cur.next = None
                    cur = None
                    return
                
            elif cur.data == key and cur.next != None:
                nxt = cur.next
                prev_node.next = nxt
                nxt.prev = prev_node
                cur.prev = None
                cur.next = None
                cur = None
                return

            elif cur.data == key and cur.next == None:
                prev_node.next = None
                cur.prev = None
                cur.next = None
                cur = None
                return
                
            prev_node = cur
            cur = cur.next
  
    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev
            
    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete(cur.data)
                cur = nxt
                
    def pairs_with_sum(self, sum_val):
        cur = self.head
        p = cur.next
        pairs = []
        while cur:
            while p:
                if cur.data + p.data == sum_val:
                    pairs.append((str(cur.data), str(p.data)))
                    p = p.next
                else:
                    p = p.next
            p = cur.next
            cur = cur.next
        return pairs
               
l1 = DoublyLinkedList()
l1.append(2)
l1.append(2)
l1.append(3)
l1.append(3)
l1.append(4)
l1.append(4)
l1.prepend(1)
l1.print_list()
# l1.add_after_node(1,5)
# l1.add_before_node(1,5)
l1.print_list()
print("Remove element")
l1.delete(1)
l1.print_list()


# l1.reverse()
# print("Reverse")
# l1.print_list()
l1.remove_duplicates()
l1.print_list()