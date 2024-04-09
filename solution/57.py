from heapq import heappush, heappop


def solution(n):
    heap = []
    while n > 0:
        i = n % 10
        heappush(heap, i)
        n //= 10
    d = 1
    while heap:
        i = heappop(heap)
        n += (i * d)
        d *= 10
    return n

def solution1(n):
    d = list(str(n))
    d.sort(reverse=True)
    return int(''.join(d))

print(solution(118372))
print(solution1(118372))
