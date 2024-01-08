def hashable(name):
    p = 31
    m = 1_000_000_007
    h = 0
    for n in name:
        h = (h * p + ord(n)) % m

    return h


def solution(participant, completion):
    dic = {}
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in completion:
        dic[i] -= 1

    for k in dic.keys():
        if dic[k] > 0:
            return k

    return None


print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']))
print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))
