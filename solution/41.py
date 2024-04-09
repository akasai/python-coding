def solution(graph, source):
    num_vertices = len(graph)  # node 갯수
    distances = [float('inf')] * num_vertices  # 가중치
    distances[source] = 0  # 초기값 초기화

    predecessor = [None] * num_vertices

    for temp in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessor[v] = u

    for u in range(num_vertices):
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                return [-1]
    return [distances, predecessor]


print(solution([[(1, 4), (2, 3), (4, -6)], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)], [(2, 2)]], 0))
# 0,-2,4,3,-6 / None,2,4,1,0
print(solution([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]], 0))
# -1
