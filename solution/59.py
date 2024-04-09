from functools import cmp_to_key


def solution(arr):
    def compare(x, y):
        t1 = int(str(x) + str(y))
        t2 = int(str(y) + str(x))
        return (t1 > t2) - (t2 > t1)

    ans = ''.join(str(l) for l in sorted(arr, key=cmp_to_key(lambda x, y: compare(x, y)), reverse=True))
    return "0" if int(ans) == 0 else ans


print(solution([6, 10, 2]))  # 6210
print(solution([3, 30, 34, 5, 9]))  # 9534330
