def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


# print(insertion_sort([1, 4, 8, 11, 16, 9, 23, 2, 7, 13]))


def merge_sort(arr):
    def sort(l, h):
        if h - l < 2:
            return
        m = (h + l) // 2
        sort(l, m)
        sort(m, h)
        merge(l, m, h)

    def merge(l, m, h):
        left, right = l, m
        tmp = []

        while left < m and right < h:
            if arr[left] < arr[right]:
                tmp.append(arr[left])
                left += 1
            else:
                tmp.append(arr[right])
                right += 1
        while left < m:
            tmp.append(arr[left])
            left += 1
        while right < h:
            tmp.append(arr[right])
            right += 1

        for i in range(l, h):
            arr[i] = tmp[i - l]

    sort(0, len(arr))
    return arr


# print(merge_sort([1, 4, 8, 11, 16, 9, 23, 2, 7, 13]))


def heap_sort(arr):
    N = len(arr)

    def heapify(n, i):
        largest = i
        left = i * 2 + 1
        right = i * 2 + 2

        if left < n and arr[largest] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            heapify(n, largest)

    for i in range(N // 2 - 1, -1, -1):
        heapify(N, i)
    for i in range(N - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    return arr


# print(heap_sort([1, 4, 8, 11, 16, 9, 23, 2, 7, 13]))

from heapq import heappush, heappop, heapify


def h():
    heap = []

    heappush(heap, 10)
    heappush(heap, 5)
    heappush(heap, 20)
    heappush(heap, 1)

    print(heap)
    print(heappop(heap))
    print(heap)
    print(heappop(heap))
    print(heap)

    heap1 = []

    heappush(heap1, (3, 'A'))
    heappush(heap1, (4, 'B'))
    heappush(heap1, (1, 'C'))
    heappush(heap1, (2, 'D'))

    print(heap1)
    print(heappop(heap1))
    print(heap1)
    print(heappop(heap1))
    print(heap1)

    heap2 = [(3, 'A'), (4, 'B'), (1, 'C'), (2, 'D')]
    heapify(heap2)
    print(heap2)


def count_sort(arr):
    count = [0] * (max(arr) + 1)
    for num in arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    ans = [0] * len(arr)
    for n in arr:
        idx = count[n]
        ans[idx - 1] = n
        count[n] -= 1
    return ans

# print(count_sort([4, 7, 9, 1, 3, 5, 2, 3, 4]))
