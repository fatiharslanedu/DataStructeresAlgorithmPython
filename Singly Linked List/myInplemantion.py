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
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            return

        position = 0
        prev = None
        while cur_node is not None:
            prev = cur_node
            cur_node = cur_node.next
            if cur_node.next is not None:
                position += 1
            if pos == position:
                prev.next = cur_node.next
                cur_node = None
                return

        if cur_node is None:
            return

    def len_iterative(self):
        cur_node = self.head
        len1 = 0
        while cur_node is not None:
            len1 += 1
            cur_node = cur_node.next

        return len1

    def len_recursive(self):  # todo: without parameter
        node = self.head

        def recurse(node):
            if node is None:
                return 0
            return 1 + recurse(node.next)
        return recurse(node)

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return
        
        cur_node1 = self.head
        prev1 = None
        while cur_node1 and cur_node1.data != key1:
            prev1 = cur_node1
            cur_node1 = cur_node1.next
            
        cur_node2 = self.head
        prev2 = None
        while cur_node2 and cur_node2.data != key2:
            prev2 = cur_node2
            cur_node2 = cur_node2.next
            
        if prev1 is not None:
            prev1.next = cur_node2
        else:
            self.head = cur_node2
        
        if prev2 is not None:
            prev2.next = cur_node1
        else:
            self.head = cur_node1
        
        cur_node1.next, cur_node2.next = cur_node2.next, cur_node1.next
        
    def reverse_iterative(self):
        cur_node = self.head
        prev = None
        while cur_node:
            nxt = cur_node.next #todo: nxt is equal to temp
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt
        self.head = prev
        
    def recursive_iterative(self):
        
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)
        
        self.head = _reverse_recursive(cur=self.head, prev=None)    

    def merge_sorted(self, llist): #must be sorted two list.
        p = self.head
        q = llist.head
        s = None
        
        if not p: #todo: check the p and q are exists?
            return q
        if not q:
            return p
        
        if p and q: #todo: set first position on the lists.
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
                
        new_head = s #todo: set the new_head
        print("new_head",new_head.data)
        while p and q: #todo: traverse on the list.
            if p.data <= q.data:
                s.next = p #todo: keep the p
                s = p
                p = s.next
            else:
                s.next = q #todo: keep the q
                s = q
                q = s.next
        
        if not p: #todo: after the operation set the final step
            s.next = q
        if not q:
            s.next = p
        self.head = new_head #todo: set the head.
        print("new_head",new_head.data)
        return self.head        

    def remove_dublicates(self):
        cur_node = self.head
        prev = None
        dup_values = {}
        while cur_node:
            if cur_node.data not in dup_values:
                prev = cur_node
                dup_values[cur_node.data] = 1
            else:
                prev.next = cur_node.next
                cur_node = None
                
            cur_node = prev.next
        
    def print_nth_from_last(self, n):
        total_len = self.len_iterative()
        
        cur_node = self.head
        while cur_node:
            if total_len == n:
                print(cur_node.data)
                return cur_node.data
            total_len -= 1
            cur_node = cur_node.next
    
    def print_nth_from_last_pointers(self, n):
        p = self.head
        q = self.head
        length = 0
        while q:
            q = q.next
            length += 1
        iterative = length - n
        i = 0
        while p and iterative != i:
            p = p.next
            i += 1
        return p.data
            
    def count_occurences_iterative(self, data):
        cur_node = self.head
        dict1 = {}
        while cur_node:
            if cur_node.data not in dict1:
                dict1[cur_node.data] = 1
            else:
                dict1[cur_node.data] += 1
            cur_node = cur_node.next
        return dict1[data]
            
    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)
        
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
            p = prev #todo: on the pivot
            while q:
                prev = q
                q = q.next
            
            q = prev #todo: on the last element
            
            q.next = self.head
            self.head = p.next
            p.next = None
            
    def is_palindrome(self):
        p = self.head
        list_palindrome = []
        prev = None
        while p:
            list_palindrome.append(p.data)
            prev = p
            p = p.next
        return list_palindrome == list_palindrome[::-1]
            
            
            
            
            
            
l1 = LinkedList()
# l1.append(2)
# l1.append(3)
# # l1.prepend(4)
# l1.append(8)
# l1.append(9)
# l1.delete_node(4)
# l1.delete_node(5)


# todo: if we dont use while loop 'llist.insert_after_node(llist.head.next, "D")'
# l1.insert_after_node(3, 7)
# l1.delete_node_at_pos(1)

# l1.print_list()
# print("Recursive Length:", l1.len_recursive())
# print("Iterative Length:", l1.len_iterative())
# # l1.swap_nodes(4, 3)
# print("\nSwap of 4 and 3 is:",end='\n')
# l1.print_list()
# print("Reverse operation Iterative")
# reversed = l1.reverse_iterative()
# l1.print_list()
# print("Reverse operation Recursive")
# l1.recursive_iterative()
# l1.print_list()
# llist_2 = LinkedList()
# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(3)
# llist_2.append(2)
# print("Merged list")
# l1.merge_sorted(llist_2)
# l1.print_list()
# print("Remove Dublicates")
# l1.remove_dublicates()
# l1.print_list()
# print("Nth from the last")
# l1.print_nth_from_last(4)
# print("Nth from the last with pointer")
# l1.print_nth_from_last_pointers(4)

# print("Count the number of given")
# print(l1.count_occurences_iterative(3))
# print("Rotate")
# l1.rotate(3)
# l1.print_list()
# print("Palindrome")

#todo: palindrome test
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(2)
l1.append(2)
print(l1.is_palindrome())
