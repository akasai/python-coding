from itertools import combinations_with_replacement


def solution(N, info):
    maxDiff = 0
    maxCombi = None

    def calc_score(c):
        aScore, rScore = 0, 0
        for score in reversed(range(11)):
            aCnt = info[10 - score]
            rCnt = c.count(score)
            if aCnt < rCnt:
                rScore += score
            elif aCnt > 0:
                aScore += score
        return aScore, rScore

    for combi in combinations_with_replacement(range(11), N):
        aS, rS = calc_score(combi)
        diff = rS - aS
        if maxDiff < diff:
            maxDiff = diff
            maxCombi = combi

    if maxDiff > 0:
        ans = [0] * 11
        for score in maxCombi:
            ans[10 - score] += 1
        return ans
    else:
        return [-1]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
