def count_sort(arr, k):
    hash = [0] * (k + 1)

    for num in arr:
        if num <= k:
            hash[num] = 1

    return hash


def solution(a, t):
    h = count_sort(a, t)

    for num in a:
        r = t - num
        if r != num and 0 <= r <= t and h[r] == 1:
            return True
    return False


print(solution([1, 2, 3, 4, 8], 6))
print(solution([2, 3, 5, 9], 10))
