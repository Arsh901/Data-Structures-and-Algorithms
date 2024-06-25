class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert_traverse(self, node, value):
        # Used in insert function to insert a new value in the tree
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self.insert_traverse(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_traverse(node.right, value)

    def insertNode(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.insert_traverse(self.root, value)

    def PreOrder_Traversal(self):
        if not self.root:
            print("No tree exists")
            return
        def pre(root):
            if not root:
                return
            print(root.value, end= " ")
            pre(root.left)
            pre(root.right)
        pre(self.root)

    def PostOrder_Traversal(self):
        if not self.root:
            print("No tree exists")
            return
        def post(root):
            if not root:
                return
            post(root.left)
            post(root.right)
            print(root.value, end=" ")
        post(self.root)

    def InOrder_Traversal(self):
        if not self.root:
            print("No tree exists")
            return
        def inO(root):
            if not root:
                return
            inO(root.left)
            print(root.value, end=" ")
            inO(root.right)
        inO(self.root)

    def Level_Traversal(self):
        if not self.root:
            print("No tree exists")
            return
        q = [self.root]
        while q:
            print(q[0].value, end = " ")
            n = q.pop(0)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

    def search_BT(self, value):
        if not self.root:
            print("Tree doesn't exist")
            return
        else:
            self.search_traversal(self.root, value)

    def search_traversal(self, node, value):
        if node.value == value:
            print("Value found in the tree")
            return
        elif node.value > value:
            if node.left:
                self.search_traversal(node.left, value)
            else:
                print("Value not found")
                return
        else:
            if node.right:
                self.search_traversal(node.right, value)
            else:
                print("Value not found")
                return

    def find_node(self, value):
        # Returns the node of the given value. Used in delete function.
        if not self.root:
            print("Tree doesn't exist")
            return
        q = [self.root]
        while q:
            node = q.pop(0)
            if node.value == value:
                return node
            else:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return None

    def min_node_rightSubtree(self, value):
        # Finds the minimum value in the right subtree of a node whose value is given
        root = self.find_node(value)
        if root.right:
            temp = root.right
            while temp.left is not None:
                temp = temp.left
            return temp.value

    def find_parent(self, value):
        #Finds the parent node of a particular node whose value is given
        def parent(root):
            if root.value > value:
                if root.left.value == value:
                    return root
                else:
                    return parent(root.left)
            elif root.value < value:
                if root.right.value == value:
                    return root
                else:
                    return parent(root.right)
        node = parent(self.root)
        return node

    # Deletion is somewhat complex, need to write 3 separate functions for it to work and then also its internal structure is tough to complete easily
    def delete_node(self, value):
        """Delete method in BST has 3 cases:
            1. Node is a leaf - Directly remove the node without altering the rest of the tree
            2. Node has 1 child - Remove the node and join its child with the grandparent node
            3. Node has 2 children - Replace the value of the node with that of the lowest value in right subtree or highest in left subtree and delete that node
        """
        if not self.root:
            print("Tree doesn't exist")
            return
        node = self.find_node(value)

        if node is self.root and not node.left and not node.right:   # Special case when only there is only root node and has no children
            self.root = None
            return
        if not node.left and not node.right:
            parent = self.find_parent(value)
            if parent.left is node:
                parent.left = None
            elif parent.right is node:
                parent.right = None
        elif (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
            parent = self.find_parent(value)
            if node.left is not None:
                parent.left = node.left
                node.left = None
            elif node.right is not None:
                parent.right = node.right
                node.right = None
        elif node.left and node.right:
            min = self.min_node_rightSubtree(node.value)
            parent = self.find_parent(min)
            if parent.left.value == min:
                self.delete_node(min)
            elif parent.right.value == min:
                self.delete_node(min)
            node.value = min


    def delete_EntireTree(self):
        if not self.root:
            print("Tree doesn't exist")
            return
        self.root = None


t = Tree()
t.insertNode(10)
t.insertNode(5)
t.insertNode(15)
t.insertNode(30)
t.insertNode(35)
t.insertNode(12)
t.insertNode(11)
t.insertNode(6)
t.insertNode(4)
t.delete_node(10)

t.Level_Traversal()























