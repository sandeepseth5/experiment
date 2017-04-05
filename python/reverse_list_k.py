ll = [1,2,3,4]


class ListNode:
    x = None
    neighbor = None

    def __init__(self, val):
        self.x = val

root = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

root.neighbor = node2
node2.neighbor = node3
node3.neighbor = node4


def reverse(linked_list, k):
    temp = linked_list
    for i in range(k):
        if temp.neighbor is not None:
            temp = temp.neighbor
    #reverse this k part
    while linked_list.neighbor is not temp:
        nn = linked_list.neighbor
        nn2 = nn.neighbor
        nn.neighbor = linked_list

    reverse(temp.neighbor, k)
    return temp


def reverse1(linked_list):
    p = linked_list
    q = p.neighbor
    while q is not None:
        temp = q.neighbor
        q.neighbor = p
        p = q
        q = temp
    linked_list.neighbor = None
    linked_list = p
    return linked_list

l1 = root
while l1 is not None:
    print(l1.x)
    l1 = l1.neighbor

l1 = reverse1(root)

while l1 is not None:
    print(l1.x)
    l1 = l1.neighbor
