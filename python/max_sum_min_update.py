class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


def max_sum_min_update(tree):
    pair = {}
    max_sum = max_path_sum(tree, pair, 0, 0)
    traverse_tree(tree, pair, 0)
    print(pair)
    update_tree(tree, pair, 0, max_sum)
    print(pair)


def max_path_sum(tree, pair, index, _sum):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        pair[index] = (False, -1)
        return tree.data

    left = max_path_sum(tree.left, pair, index * 2 + 1, _sum + tree.data)
    right = max_path_sum(tree.right, pair, index * 2 + 2, _sum + tree.data)

    pair[index] = (False, -1)
    return max(left, right) + tree.data


def traverse_tree(tree, pair, index):
    if tree is None:
        return None
    if tree.left is None and tree.right is None:
        pair[index] = (True, tree.data)
        return True, tree.data
    left = traverse_tree(tree.left, pair, index * 2 + 1)
    right = traverse_tree(tree.right, pair, index * 2 + 2)

    if left is None and right is not None:
        pair[index] = (True, right[1] + tree.data) if right[0] is True else (False, 0)
    elif left is not None and right is None:
        pair[index] = (True, left[1] + tree.data) if left[0] is True else (False, 0)
    elif left[0] is True and right[0] is True:
        pair[index] = (True, left[1] + tree.data) if left[1] == right[1] else (False, 0)

    return pair[index]


def update_tree(tree, pair, index, max_sum):
    if tree is None:
        return
    update_tree(tree.left, pair, 2 * index + 1, max_sum)
    update_tree(tree.right, pair, 2 * index + 2, max_sum)

    if pair[index][0] is False and pair[2 * index + 1][0] is True and pair[2 * index + 2][0] is True:
        diff = abs(pair[2 * index + 1][1] - pair[2 * index + 2][1])
        if pair[2 * index + 1][1] < pair[2 * index + 2][1]:
            pair[2 * index + 1] = (True, pair[2 * index + 1][1] + diff)
            tree.left.data += diff
        else:
            pair[2 * index + 2] = (True, pair[2 * index + 2][1] + diff)
            tree.right.data += diff
        pair[index] = (True, pair[2 * index + 1][1] + tree.data)


def print_tree(tree):
    if tree is not None:
        print_tree(tree.left)
        print(tree.data, end=" ")
        print_tree(tree.right)


root = Node(5)
a7 = Node(7)
a10 = Node(10)
a3 = Node(3)
a9 = Node(9)
a1 = Node(1)
a4 = Node(4)
a6 = Node(6)
a5 = Node(5)
a2 = Node(2)

root.left = a7
root.right = a10
a7.left = a3
a7.right = a9
a10.left = a1
a10.right = a4
a9.right = a6
a1.right = a5
a4.left = a2

max_sum_min_update(root)

print_tree(root)
