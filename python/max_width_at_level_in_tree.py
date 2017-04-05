class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

leftIndex = 9999
rightIndex = -1


def max_width(tree, index, height, level):
    global leftIndex
    global rightIndex
    if tree is None or height > level:
        return
    if height < level:
        max_width(tree.left, index * 2 + 1, height+1, level)
        max_width(tree.right, index * 2 + 2, height+1, level)

    if height == level:
        leftIndex = min(leftIndex, index)
        rightIndex = max(rightIndex, index)

tree = Node(0)
a = Node(3)
b = Node(5)
c = Node(0)
d = Node(0)
e = Node(0)
f = Node(0)
tree.left = a
tree.right = b

a.left = c
c.left = e
b.left= d
d.right = f

print(max_width(tree, 0, 0, 3))

print(leftIndex)
print(rightIndex)