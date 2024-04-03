class RedBlackTreeNode:
    def __init__(self, value, color="RED"):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class MyRedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = RedBlackTreeNode(value, color="BLACK")
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = RedBlackTreeNode(value)
                node.left.parent = node
                self._fix_insertion(node.left)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = RedBlackTreeNode(value)
                node.right.parent = node
                self._fix_insertion(node.right)
            else:
                self._insert_recursive(node.right, value)

    def _fix_insertion(self, node):
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._left_rotate(node.parent.parent)
        self.root.color = "BLACK"

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node):
        result = []
        if node:
            result += self._inorder_traversal_recursive(node.left)
            result.append(node.value)
            result += self._inorder_traversal_recursive(node.right)
        return result

# Test the Red-Black Tree
my_rbt = MyRedBlackTree()
my_rbt.insert(5)
my_rbt.insert(3)
my_rbt.insert(7)
my_rbt.insert(2)
my_rbt.insert(4)
my_rbt.insert(6)
my_rbt.insert(8)
print( my_rbt.inorder_traversal())  # output [2, 3, 4, 5, 6, 7, 8]
