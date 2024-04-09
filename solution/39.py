from collections import defaultdict, deque


def solution(graph, start):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    def bfs(start):
        ans = []
        visited = set()  # 방문한 노드 -> 재방문 방지

        q = deque([start])  # 방문 할 노드를 저장하는 q
        ans.append(start)
        visited.add(start)

        while q:
            node = q.popleft()
            for n in adj_list.get(node, []):
                if n not in visited:
                    ans.append(n)
                    visited.add(n)
                    q.append(n)
        return ans

    return bfs(start)


# 1,2,3,4,5,6,7,8,9
print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)], 1))
# 1,2,3,4,5,0
print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1))
