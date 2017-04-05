class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bottom_view(tree):
    dic = {}
    # dic = {i: None for i in range(col)}
    print(dic)
    traverse(tree, 0, 0, dic)
    print(dic)


def traverse(tree, level, index, dic):
    if tree is None:
        return
    if dic.get(index, None) is not None:
        if level > dic[index][0]:
            dic[index] = (level, tree.data)
    else:
        dic[index] = (level, tree.data)
    traverse(tree.left, level+1, index-1, dic)
    traverse(tree.right, level+1, index+1, dic)

def height(tree):
    if tree is None:
        return 0
    return 1 + max(height(tree.left), height(tree.right))


tree = Node(0)
a = Node(3)
b = Node(5)
c = Node(4)
d = Node(6)
e = Node(7)
f = Node(8)
tree.left = a
tree.right = b

a.left = c
c.left = e
b.left= d
d.right = f

print(height(tree))
bottom_view(tree)