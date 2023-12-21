def solution(n, stages):
    """
    stage와 인덱스를 통일시키기 위한 buffer (+1)
    n스테이지를 통과한 인원 (+1)
    """
    c = [0] * (n + 2)

    for s in stages:
        c[s] += 1  # 현재 진행 중인 스테이지에 있는 사람 수

    failRate = {}  # 스테이지 실패율
    total = len(stages)  # 총 인원 수

    for i in range(1, n + 1):
        if c[i] == 0:  # 도전자가 없으면
            failRate[i] = 0
        else:
            failRate[i] = c[i] / total
            total -= c[i]

    result = sorted(failRate, key=lambda x: failRate[x], reverse=True)

    return result


result = solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
# result = solution(4, [4, 4, 4, 4, 4])
print(result)
