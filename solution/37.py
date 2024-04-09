def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])  # 경로 압축 => 루트노드로 세팅
    return parent[i]


"""
랭크 기준으로 병합
"""
def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:  # y가 x보다 깊으면 = 노드가 더 많이 달려있으면 => y에 x를 단다.
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]: # x가 y보다 깊으면 => x에 y를 단다.
        parent[y_root] = x_root
    else: # 같으면 둘 중 하나에 달고 루트에 랭크를 늘린다.
        parent[y_root] = x_root
        rank[x_root] += 1


def solution(n, costs):
    costs.sort(key=lambda x: x[2])  # cost 낮은 순으로 정렬

    parent = [i for i in range(n)]  # 각 노드들의 부모노드 세팅
    rank = [0] * n  # 각 노드의 랭크

    min_cost, edges = 0, 0

    for edge in costs:
        if edges == n - 1: # n개의 노드를 잇는 길은 n-1
            break

        x = find(parent, edge[0])
        y = find(parent, edge[1])

        if x != y:
            union(parent, rank, x, y)
            min_cost += edge[2]
            edges += 1

    return min_cost


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
