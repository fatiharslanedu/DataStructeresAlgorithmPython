class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
class BST(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def insert(self, new_val):
        self.insert_helper(self.root, new_val)
    
    def insert_helper(self, current, new_val):
        if current.data < new_val: #todo: check for right side
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)
        
    def search(self, find_value):
        return self.search_helper(self.root, find_value)
        
    def search_helper(self, current, find_value):
        if current:
            if current.data == find_value:               
                return True
            elif current.data < find_value:
                return self.search_helper(current.right, find_value)
            else:
                return self.search_helper(current.left, find_value)
    
    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)
            
    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)
            
            
    def is_bst_satisfied(self):
        return self.is_bst_satisfied_helper(self.root)
    
    def is_bst_satisfied_helper(self, current):
        if current:
            if current.left.data < current.data:
                return self.is_bst_satisfied_helper(current.left.data)
            elif current.right.data > current.data:
                return self.is_bst_satisfied_helper(current.right.data)
            else:
                return False
        return True
                
                
                
def BSTinsertSearch():
    bst = BST(10)
    bst.insert(3)                
    bst.insert(1)                
    bst.insert(25)                
    bst.insert(9)                
    bst.insert(13)
    print(bst.search(9))    
    print(bst.search(14))   
    print(bst.is_bst_satisfied())      
                 
                
def main():
    BSTinsertSearch()         
   
            
if __name__ == "__main__":
    main()