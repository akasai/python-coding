def solution(nodes):
    return [
        preorder(nodes, 0)[:-1],
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1]
    ]


def preorder(nodes, idx):
    if idx < len(nodes):
        ret = str(nodes[idx]) + " "
        ret += preorder(nodes, idx * 2 + 1)
        ret += preorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""


def inorder(nodes, idx):
    if idx < len(nodes):
        ret = inorder(nodes, idx * 2 + 1)
        ret += str(nodes[idx]) + " "
        ret += inorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""


def postorder(nodes, idx):
    if idx < len(nodes):
        ret = postorder(nodes, idx * 2 + 1)
        ret += postorder(nodes, idx * 2 + 2)
        ret += str(nodes[idx]) + " "
        return ret
    else:
        return ""


print(solution([1, 2, 3, 4, 5, 6, 7]))
# preorder: 1 2 4 5 3 6 7
# inorder: 4 2 5 1 6 3 7
# postorder: 4 5 2 6 7 3 1
"""
  1
 2 3
45 67
"""
