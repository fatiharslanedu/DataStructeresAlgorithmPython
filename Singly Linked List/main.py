class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        # todo: if not None
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exists.")
            return

        new_node = Node(data)
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == prev_node:
                break
            cur_node = cur_node.next

        new_node.next = cur_node.next
        cur_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node.data == key and cur_node == self.head:
            self.head = cur_node.next
            cur_node = None  # todo: delete operation
            return

        prev = None

        while cur_node is not None and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:  # todo: if we cannot find
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return
        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
        print("last",prev.data)
        
    def recursive_reverse(self):
        
        def _rec(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _rec(cur, prev)
        self.head = _rec(cur = self.head, prev = None)      

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        
        if not p:
            return q
        if not q:
            return p
        
        if p and q: #todo: for create the s (*other pointer)
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
        new_head = s
        
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
            
        if not p:
            s.next = q
        if not q:
            s.next = p
        self.head = new_head    
        
        return self.head
    
    def remove_dublicates(self):
        cur_node = self.head
        dup_values = {}
        prev = None
        while cur_node:
            if cur_node.data in dup_values:
                prev.next = cur_node.next
                cur_node = None
            else:
                dup_values[cur_node.data] = 1
                prev = cur_node
            cur_node = prev.next
            
    def print_nth_from_last(self, n):
        total_len = self.len_iterative()
        cur_node = self.head
        while cur_node:
            if n == total_len:
                print(cur_node.data)
                return cur_node.data
            total_len -= 1
            cur_node = cur_node.next
        if cur_node is None:
            return
        
    def print_nth_from_last_pointers(self, n):
        p = self.head
        q = self.head
        
        if n > 0:
            count = 0
            while q:
                count += 1
                if (count >= n):
                    break
                q = q.next
            
            if not q:
                print(str(n) + " is greater than the number of nodes in list.")
                return
            while p and q.next:
                p = p.next
                q = q.next
            return p.data
                
    def print_nth_from_last2(self, n, method):
        if method == 1:
            #Method 1:
            total_len = self.len_iterative()
            cur = self.head 
            while cur:
                if total_len == n:
                   #print(cur.data)
                    return cur.data
                total_len -= 1
                cur = cur.next
            if cur is None:
                return

        elif method == 2:
            # Method 2:
            p = self.head
            q = self.head

            if n > 0:
                count = 0
                while q:
                    count += 1
                    if(count>=n):
                        break
                    q = q.next
                    
                if not q:
                    print(str(n) + " is greater than the number of nodes in list.")
                    return

                while p and q.next:
                    p = p.next
                    q = q.next
                return p.data
            else:
                return None
            
    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0
            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev
            q.next = self.head
            self.head = p.next
            p.next = None
            
    def is_palindrome(self):
        p = self.head
        list_palindrome = []
        while p:
            list_palindrome.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = list_palindrome.pop()
            if data != p.data:
                return False
            p = p.next
        return True
    
    
            

llist_1 = LinkedList()
llist_1.append(2)
llist_1.append(3)
# llist_1.prepend(4)
llist_1.append(8)
# l1.delete_node(4)
# l1.delete_node(5)


# # todo: if we dont use while loop 'llist.insert_after_node(llist.head.next, "D")'
# # l1.insert_after_node(3, 7)
# llist_1.delete_node_at_pos(1)

# llist_1.print_list()
# print("The length of the linked list calculated recursively after inserting 4 elements is:")
# print(llist_1.len_recursive(llist_1.head))
# print("The length of the linked list calculated iteratively after inserting 4 elements is:")
# print(llist_1.len_iterative())
# llist_1.reverse_iterative()
# print("Reversed iterative:")
# llist_1.print_list()
# print("Reversed recursive:")
# llist_1.recursive_reverse()
# llist_1.print_list()

llist_2 = LinkedList()

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)
print("\nLinked list2:")
llist_2.print_list()
llist_1.merge_sorted(llist_2)
print("\nMerged:")
llist_1.print_list()
print("Nth from the last")
llist_1.print_nth_from_last(5)
print("Nth from the last with pointer")
llist_1.print_nth_from_last_pointers(5)
print("Rotate")
llist_1.rotate(4)
llist_1.print_list()