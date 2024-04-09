from heapq import heappush, heappop


def solution(n, road, k):
    # graph 세팅
    graph = [[] for _ in range(n + 1)]  # 인덱스를 편하게 하기 위해 +1
    for a, b, cost in road:
        # 양방향
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    # 소요값 세팅
    ds = [float('inf')] * (n + 1)
    ds[1] = 0

    # 우선순위 큐
    heapq = []
    heappush(heapq, (0, 1))

    while heapq:
        dist, node = heappop(heapq)

        for next_node, next_cost in graph[node]:
            d = dist + next_cost
            if d <= ds[next_node]:
                ds[next_node] = d
                heappush(heapq, (d, next_node))

    return sum(1 for d in ds if d <= k)


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))  # 4
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))  #
