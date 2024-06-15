class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def PreOrder_traversal(root):
    if not root:
        return
    print(root.value, end=" ")
    PreOrder_traversal(root.left)
    PreOrder_traversal(root.right)


def InOrder_Traversal(root):
    if not root:
        return
    InOrder_Traversal(root.left)
    print(root.value, end=" ")
    InOrder_Traversal(root.right)


def PostOrder_Traversal(root):
    if not root:
        return
    PostOrder_Traversal(root.left)
    PostOrder_Traversal(root.right)
    print(root.value, end=" ")


def Level_Order_Traversal(root):
    if not root:
        return
    else:
        queue = []
        queue.append(root)
        while (len(queue) > 0):
            print(queue[0].value, end=" ")
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


def Search_BT(root, value):
    if not root:
        return "Tree doesn't exist"
    else:
        queue = []
        level = 0
        queue.append(root)
        while len(queue) > 0:
            if queue[0].value == value:
                return f"\nTarget Value found in level {level}"
            else:
                level += 1
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
    return False


def insert_nodes(root, new_node):
    if not root:
        root = new_node
    else:
        queue = []
        queue.append(root)
        while len(queue) > 0:
            if queue[0].left is None:
                queue[0].left = new_node
                break
            elif queue[0].right is None:
                queue[0].right = new_node
                break
            else:
                node = queue.pop(0)
                queue.append(node.left)
                queue.append(node.right)


def deepest_Node(root):
    if not root:
        return "Tree doesn't exist"
    else:
        q = [root]
        node = None
        while len(q)>0:
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
    return node


# Nodes cannot be deleted from a BT directly. We need to replace the deletion node value with the deepest node value and then delete the deepest node.
def delete_node(root, node):
    if not root:
        return "Tree doesn't exist"
    if not Search_BT(root, node.value):
        return "Value not found in Tree"
    d_node = deepest_Node(root)
    node.value = d_node.value
    q = [root]
    while q:
        current = q.pop(0)
        if current.left:
            if current.left == d_node:
                current.left = None
                break
            else:
                q.append(current.left)
        if current.right:
            if current.right == d_node:
                current.right = None
                break
            else:
                q.append(current.right)


def delete_all(root):
    root.value = None
    root.left = None
    root.right = None



D = TreeNode("Drinks")
H = TreeNode("Hot")
C = TreeNode("Cold")
T = TreeNode("Tea")
Cof = TreeNode("Coffee")

D.left = H
D.right = C
H.left = T
H.right = Cof

P = TreeNode("Pepsi")
Cola = TreeNode("COLA")
insert_nodes(D, P)
insert_nodes(D, Cola)
Level_Order_Traversal(D)
delete_node(D, D)
Level_Order_Traversal(D)