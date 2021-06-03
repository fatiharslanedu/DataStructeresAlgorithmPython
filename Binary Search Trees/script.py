class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
        
class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root) 
        
    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
                
        else:
            print("Value already in tree!")                
            
    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)
            
    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)
            
    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None
        
    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True
        
    def is_bst_satisfied(self):
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.data
            if val <= lower or val >= upper:
                return False
            
            if not helper(node.right, val, upper):
                return False
            
            if not helper(node.left, lower, val):
                return False
            
            return True
        return helper(self.root)
        

def intro():
    bst = BST(7)
    bst.insert(3)
    bst.insert(10)
    bst.insert(5)
    bst.insert(1)
    bst.insert(8)
    bst.insert(9)
    bst.insert(2)

    bst.inorder_print_tree()         
    print(bst.find(2))

def main():
    intro()


if __name__ == "__main__":
    main()