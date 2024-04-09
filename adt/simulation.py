m1 = [[4, 5, 1], [3, 6, 2], [2, 5, 4]]
m2 = [[1, 5, 2], [3, 2, 6], [3, 4, 2]]


def add(a, b):
    return [[a[row][col] + b[row][col] for col in range(len(a[row]))] for row in range(len(a))]


def dis(a, b):
    return [[a[row][col] - b[row][col] for col in range(len(a[row]))] for row in range(len(a))]


print(add(m1, m2))
print(dis(m1, m2))

m3 = [[4, 5, 1, 1], [3, 6, 2, 2], [2, 5, 4, 4]]
m4 = [[1, 5, 2], [3, 2, 6], [3, 4, 2], [5, 2, 3]]


def multi(a, b):
    if len(a[0]) != len(b):
        return

    ans = [[0] * len(b[0]) for _ in range(len(a))]

    for i, row in enumerate(a):
        for j in range(len(b[0])):
            ans[i][j] = sum([b[k][j] * row[k] for k in range(len(row))])

    return ans


def reverse(a):
    return [[a[j][i] for j in range(len(a[0]))] for i in range(len(a))]


print(multi(m3, m4))
print(reverse([[4, 5, 1], [3, 6, 2], [2, 5, 4]]))


def ordinate(x, y):
    N = 5
    m = [[0] * N for _ in range(N)]
    m[y][x] = 1
    for r in m:
        print(r)


ordinate(3, 4)


def sym(a):
    N = len(a[0])
    return [[a[i][(N - 1) - j] for j in range(len(a[0]))] for i in range(len(a))]


def rotate(a, d):
    N = len(a[0])
    ans = a.copy()
    for _ in range(0, d, 90):
        ans = [[ans[j][(N - 1) - i] for j in range(len(ans[0]))] for i in range(len(ans))]
    return ans


print(sym(m1))
print(rotate([[4, 3, 2], [5, 6, 5], [1, 2, 4]], 180))
