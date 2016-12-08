#encoding=utf-8

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return '<Node %s>' % (self.value, )

class BinaryTree:
    def __init__(self):
        self.root = None

    def initTree(self, li):
        node_list = [TreeNode(value) for value in li]
        for index, node in enumerate(node_list, 1):
            parent_index, position = index / 2 - 1, index % 2
            if parent_index == -1:
                self.root = node
            elif position == 0:
                node_list[parent_index].left = node
            else:
                node_list[parent_index].right = node

    @staticmethod
    def createTreePreOrder(root, li):
        if not li or li[0] is None:
            root = None
        else:
            root = TreeNode(li[0])
            del li[0]
            BinaryTree.createTreePreOrder(root.left, li)
            BinaryTree.createTreePreOrder(root.right, li)
        return root


    @staticmethod
    def preOrderVisit(root, visit_func):
        if root:
            visit_func(root)
            BinaryTree.preOrderVisit(root.left, visit_func)
            BinaryTree.preOrderVisit(root.right, visit_func)

    @staticmethod
    def midOrderVisit(root, visit_func):
        if root:
            BinaryTree.midOrderVisit(root.left, visit_func)
            visit_func(root)
            BinaryTree.midOrderVisit(root.right, visit_func)

    @staticmethod
    def afterOrderVisit(root, visit_func):
        if root:
            BinaryTree.afterOrderVisit(root.left, visit_func)
            BinaryTree.afterOrderVisit(root.right, visit_func)
            visit_func(root)

    @staticmethod
    def nonrecMidOrderVisit(root, visit_func):
        stack = [root]
        while stack:
            cur = stack[-1]
            while cur:
                stack.append(cur.left)
                #visit_func(cur)  # 先序遍历
                cur = cur.left
            stack.pop()
            if stack:
                cur = stack.pop()
                #visit_func(cur)  # 中序遍历
                stack.append(cur.right)

    @staticmethod
    def nonrecMidOrderVisit2(root, visit_func):
        p = root
        stack = []
        while(p or stack):
            if p:
                stack.append(p)
                p = p.left
            else:
                rot = stack.pop()
                visit_func(rot)
                p = rot.right

def visit_node(node):
    print node.value

def test():
    tree = BinaryTree()
    #tree.initTree(range(15))
    #tree.preOrderVisit(tree.root, visit_node)
    #tree.midOrderVisit(tree.root, visit_node)
    #tree.afterOrderVisit(tree.root, visit_node)
    #tree.nonrecMidOrderVisit2(tree.root, visit_node)
    root = BinaryTree.createTreePreOrder(tree.root, ['A', 'B', 'C', None, None, 'D', 'E', None, 'G', None, None, 'F', None, None, None])
    BinaryTree.preOrderVisit(root, visit_node)

test()
