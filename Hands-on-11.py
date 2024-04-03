class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class MyBinarySearchTree:
    def __init__(self):
        self.root_node = None

    def insert(self, key):
        if not self.root_node:
            self.root_node = TreeNode(key)
        else:
            self._insert_recursive(self.root_node, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root_node, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root_node)

    def _inorder_traversal_recursive(self, node):
        result = []
        if node:
            result += self._inorder_traversal_recursive(node.left)
            result.append(node.key)
            result += self._inorder_traversal_recursive(node.right)
        return result

# Test the Binary Search Tree
my_bst = MyBinarySearchTree()
my_bst.insert(5)
my_bst.insert(3)
my_bst.insert(7)
my_bst.insert(2)
my_bst.insert(4)
my_bst.insert(6)
my_bst.insert(8)
print( my_bst.inorder_traversal())  # output [2, 3, 4, 5, 6, 7, 8]
print(my_bst.search(4).key)  # output 4
