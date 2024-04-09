from heapq import heappush, heappop


def solution(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    q = []
    heappush(q, [0, start])
    paths = {start: [start]}

    while q:
        cur_dist, cur_node = heappop(q)  # 가장 작은 거리값 가져옴

        if distances[cur_node] < cur_dist:
            continue

        for adj_node, weight in graph[cur_node].items():
            dist = cur_dist + weight

            if distances[adj_node] > dist:
                distances[adj_node] = dist
                heappush(q, [dist, adj_node])
                paths[adj_node] = paths[cur_node] + [adj_node]

    sorted_path = {node: paths[node] for node in sorted(paths)}
    return [distances, sorted_path]


print(solution({'a': {'b': 9, 'c': 3}, 'b': {'a': 5}, 'c': {'b': 1}}, 'a'))
# print(solution({'a': {'b': 1}, 'b': {'c': 5}, 'c': {'d': 1}, 'd': {}}, 'a'))
