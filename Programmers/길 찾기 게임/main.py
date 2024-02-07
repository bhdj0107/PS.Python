import sys
sys.setrecursionlimit(10**8)
class BinaryTree:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def create(self, value):
        self.value = value
        self.left = BinaryTree()
        self.right = BinaryTree()
        return self
    def preorder(self):
        if self.value:
            return [self.value] + self.left.preorder() + self.right.preorder()
        else:
            return []

    def postorder(self):
        if self.value:
            return self.left.postorder() + self.right.postorder() + [self.value]
        else:
            return []

height_order = [[]]
globalnodeinfo = [(0,0,0)]
all_nodes = []
def set_children(idx, my_height, l_limit, r_limit):
    me = all_nodes[idx]
    left, right = BinaryTree(), BinaryTree()
    for nextguess in height_order[my_height + 1]:
        if l_limit <= globalnodeinfo[nextguess][1] < globalnodeinfo[idx][1]:
            left = all_nodes[nextguess]

        if globalnodeinfo[idx][1] < globalnodeinfo[nextguess][1] <= r_limit:
            right = all_nodes[nextguess]

    all_nodes[idx].left = left
    all_nodes[idx].right = right
    if left.value:
        set_children(left.value, my_height + 1, l_limit, globalnodeinfo[idx][1]-1)
    if right.value:
        set_children(right.value, my_height + 1, globalnodeinfo[idx][1] + 1, r_limit)

def solution(nodeinfo):
    global height_order, all_nodes, globalnodeinfo
    all_nodes = [BinaryTree.create(BinaryTree(), value=i) for i in range(len(nodeinfo) + 1)]

    temp = [(0,0,0)]
    setidx = [False for _ in range(len(nodeinfo) + 1)]
    for i, xy in enumerate(nodeinfo):
        temp.append([i + 1, xy[0], xy[1]])
    globalnodeinfo = temp

    temp = sorted(globalnodeinfo[1:], key=lambda x:x[2], reverse=True)
    nowh = temp[0][2]
    for idx_nodeinfo in temp:
        if nowh > idx_nodeinfo[2]:
            nowh = idx_nodeinfo[2]
            height_order.append([])
        height_order[-1].append(idx_nodeinfo[0])

    height_order.append([])
    root = all_nodes[height_order[0][0]]
    set_children(root.value, 0, 0, 100001)

    return [root.preorder(), root.postorder()]
