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
        u"""用从上到下，从左到右的方式，初始化二叉树."""
        node_list = [TreeNode(value) for value in li]
        for index, node in enumerate(node_list, 1):
            parent_index, position = index / 2 - 1, index % 2
            if parent_index == -1:
                self.root = node
            elif position == 0:
                node_list[parent_index].left = node
            else:
                node_list[parent_index].right = node

    # 按照C语言的思路写按照先序遍历的顺序创建二叉树会有问题
    # 由于python语言并没有指针的概念，所以无法指示在树的哪一边创建节点
    #def createTreePreOrder(self, root, li):
    #    if not li or li[0] is None:
    #        root = None
    #    else:
    #        root = TreeNode(li[0])
    #        del li[0]
    #        self.createTreePreOrder(root.left, li, left=True)
    #        self.createTreePreOrder(root.right, li, left=False)
    #    return root

    def createAsPreOrder(self, li):
        u"""给定一个二叉树，可以明确写出其先序的遍历顺序；反之，则不能，除非要将叶子节点标示出来。
        如给定ABCDEF作为先序序列，是无法得知树的结构，要给定诸如['A', 'B', 'C', None, None,
        'D', 'E', None, 'G', None, None, 'F', None, None, None]这样的序列才能确定二叉树的结构."""

        if not li or li[0] is None:
            return
        self.root = TreeNode(li[0])
        del li[0]
        self._createAsPreOrder(self.root, li, left=True)
        self._createAsPreOrder(self.root, li, left=False)


    def _createAsPreOrder(self, parent, li, left):
        if li:
            # 注释下面三行，会把None也当做TreeNode处理
            if li[0] is None:
                del li[0]
                return

            if left:
                parent.left = TreeNode(li[0])
                p = parent.left
            else:
                parent.right = TreeNode(li[0])
                p = parent.right
            del li[0]
            self._createAsPreOrder(p, li, left=True)
            self._createAsPreOrder(p, li, left=False)


    def preOrderVisit(self, root, visit_func):
        if root:
            visit_func(root)
            self.preOrderVisit(root.left, visit_func)
            self.preOrderVisit(root.right, visit_func)

    def midOrderVisit(self, root, visit_func):
        if root:
            self.midOrderVisit(root.left, visit_func)
            visit_func(root)
            self.midOrderVisit(root.right, visit_func)

    def afterOrderVisit(self, root, visit_func):
        if root:
            self.afterOrderVisit(root.left, visit_func)
            self.afterOrderVisit(root.right, visit_func)
            visit_func(root)

    def nonrecMidOrderVisit(self, root, visit_func):
        u"""一个版本的中序和先序遍历."""
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
                visit_func(cur)  # 中序遍历
                stack.append(cur.right)

    def nonrecMidOrderVisit2(self, root, visit_func):
        u"""另一个版本的中序和先序遍历."""
        p = root
        stack = []
        while(p or stack):
            if p:
                stack.append(p)
                #visit_func(p)  # 先序遍历
                p = p.left
            else:
                rot = stack.pop()
                visit_func(rot)  # 中序遍历
                p = rot.right

    # 后序遍历的非递归版本比较复杂，需要为每一个节点创建一个标示，标示被访问过。


def visit_node(node):
    print node.value

def test_binary_tree():
    tree = BinaryTree()
    #tree.initTree(range(15))
    #tree.preOrderVisit(tree.root, visit_node)
    #tree.midOrderVisit(tree.root, visit_node)
    #tree.afterOrderVisit(tree.root, visit_node)
    #tree.nonrecMidOrderVisit2(tree.root, visit_node)
    #tree.createAsPreOrder(['A', 'B', 'C', None, None, 'D', 'E', None, 'G', None, None, 'F', None, None, None])
    #tree.nonrecMidOrderVisit(tree.root, visit_node)
    tree.nonrecMidOrderVisit2(tree.root, visit_node)


class HoffmanTree(BinaryTree):

    def create(self, values):
        u"""根据列表创建霍夫曼树.

        values是列表，列表中元素包含两个部分，一个是name，一个是权重."""

        if not values: return
        if len(values) < 2:
            self.root = TreeNode(values[0])
            return self.root

        nodes = [TreeNode(value) for value in values]
        nodes.sort(key=lambda x: x.value[1])

        while len(nodes) > 1:
            node_l, node_r, nodes = nodes[0], nodes[1], nodes[2:]
            node_new = TreeNode(('tmp', node_l.value[1] + node_r.value[1]), node_l, node_r)

            for i, n in enumerate(nodes):
                if n.value[1] > node_new.value[1]:
                    nodes.insert(i, node_new)
                    break
            else:
                nodes.append(node_new)

        self.root = nodes[0]
        return self.root

    def getHoffmanCoding(self, node, prefix=''):
        u"""获取霍夫曼编码(递归方式)."""
        if not node.left and not node.right:
            print node.value, '-->', prefix
        else:
            self.getHoffmanCoding(node.left, prefix + '0')
            self.getHoffmanCoding(node.right, prefix + '1')


def test_hoffman_tree():
    values = [('A', 5), ('B', 29), ('C', 7), ('D', 8), ('E', 14), ('F', 23), ('G', 3), ('H', 11)]
    tree = HoffmanTree()
    tree.create(values)
    #tree.nonrecMidOrderVisit2(tree.root, visit_node)
    tree.getHoffmanCoding(tree.root)


test_hoffman_tree()
