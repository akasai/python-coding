from collections import defaultdict


def solution(graph, start):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    def dfs(node, visited, result):
        visited.add(node)
        result.append(node)
        for n in adj_list.get(node, []):
            if n not in visited:
                dfs(n, visited, result)

    visited = set()
    ans = []
    dfs(start, visited, ans)
    return ans


# print(solution([['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e']], 'a'))  # a,b,c,d,e
print(solution([['a', 'f'], ['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e']], 'a'))  # a,b,c,d,e
# print(solution([['a', 'b'], ['a', 'c'], ['b', 'd'], ['b', 'e'], ['c', 'f'], ['e', 'f']], 'a'))  # a,b,d,e,f,c
