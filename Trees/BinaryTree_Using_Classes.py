class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def PreOrder_Traversal(self):
        if not self.root:
            print("No tree")
            return
        def pre(root):
            if not root:
                return
            print(root.value, end=" ")
            pre(root.left)
            pre(root.right)
        pre(self.root)

    def InOrder_Traversal(self):
        if not self.root:
            print("No tree")
            return
        def In(root):
            if not root:
                return
            In(root.left)
            print(root.value, end=" ")
            In(root.right)
        In(self.root)

    def PostOrder_Traversal(self):
        if not self.root:
            print("No tree")
            return
        def post(root):
            if not root:
                return
            post(root.left)
            post(root.right)
            print(root.value, end=" ")
        post(self.root)


    def Level_traversal(self):
        if not self.root:
            print("No tree")
            return
        q = []
        q.append(self.root)
        while len(q)>0:
            print(q[0].value, end=" ")
            n = q.pop(0)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

    def insertNode(self, value):
        node = TreeNode(value)
        if not self.root:
            self.root = node
        else:
            q = []
            q.append(self.root)
            while len(q) > 0:
                n = q.pop(0)
                if n.left is None:
                    n.left = node
                    break
                elif n.right is None:
                    n.right = node
                    break
                else:
                    q.append(n.left)
                    q.append(n.right)


    def search_BT(self, value):
        if not self.root:
            print("No tree")
            return
        q = []
        q.append(self.root)
        while len(q)>0:
            if q[0].value == value:
                print(f"\nValue found in the tree")
                return
            else:
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        print("\nValue not found in the tree")

    def deepest_node(self):
        if not self.root:
            print("No tree")
            return
        q = [self.root]
        node = None
        while len(q)>0:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return node

    def find_node(self, value):
        if not self.root:
            print("No tree")
            return
        q = [self.root]
        while len(q)>0:
            node = q.pop(0)
            if node.value == value:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return None

    def delete_node(self, value):
        if not self.root:
            print("No tree")
            return
        node = self.find_node(value)
        if not node:
            print("Value not found inside the tree")
            return
        if self.root == node and not self.root.left and not self.root.right:
            self.root = None
            return
        d_node = self.deepest_node()
        node.value = d_node.value
        q = [self.root]
        while q:
            curr = q.pop(0)
            if curr.left:
                if curr.left == d_node:
                    curr.left = None
                    break
                q.append(curr.left)
            if curr.right:
                if curr.right == d_node:
                    curr.right = None
                    break
                q.append(curr.right)


    def delete_tree(self):
        if not self.root:
            print("Tree doesn't exist")
            return
        self.root = None


t = Tree()
t.insertNode(1)
t.insertNode(2)
t.insertNode(3)
t.insertNode(4)
t.insertNode(5)
t.insertNode(6)