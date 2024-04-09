class Node:
    def __init__(self, x, y, n):
        self.value = (x, y)
        self.num = n
        self.left = None
        self.right = None


class BT:
    def __init__(self):
        self.root = None

    def insert(self, x, y, n):
        if not self.root:
            self.root = Node(x, y, n)
        else:
            curr = self.root
            while True:
                if curr.value[0] > x:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(x, y, n)
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(x, y, n)
                        break


def post_order(bt):
    stack = [(bt.root, False)]  # (node, visited)
    ans = []
    while stack:
        n, v = stack.pop()
        if n is None:
            continue
        if v:
            ans.append(n.num)
        else:
            stack.append((n, True))
            stack.append((n.right, False))
            stack.append((n.left, False))

    return ans


def pre_order(bt):
    stack = [bt.root]
    ans = []
    while stack:
        node = stack.pop()
        if node is None:
            continue
        stack.append(node.left)  # left부터 순회.
        stack.append(node.right)
        ans.append(node.num)

    return ans


def solution(nodeinfo):
    nodes = [(nodeinfo[i][0], nodeinfo[i][1], i + 1) for i in range(len(nodeinfo))]
    nodes = sorted(nodes, key=lambda n: n[1], reverse=True)
    bt = BT()

    for x, y, n in nodes:
        bt.insert(x, y, n)

    return [pre_order(bt), post_order(bt)]


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
