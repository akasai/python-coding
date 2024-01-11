def solution(want, number, discount):
    want_dic = {}
    for i, k in enumerate(want):
        want_dic[k] = number[i]

    cnt = 0
    for i in range(len(discount) - 9):
        dic = {}
        for d in discount[i:i + 10]:
            if d in want_dic:
                dic[d] = dic.get(d, 0) + 1

        if want_dic == dic:
            cnt += 1

    return cnt


print(solution(['banana', 'apple', 'rice', 'pork', 'pot'], [3, 2, 2, 2, 1],
               ['chicken', 'apple', 'apple', 'banana', 'rice', 'apple', 'pork', 'banana', 'pork', 'rice', 'pot',
                'banana', 'apple', 'banana']))  # 3
print(solution(['apple'], [10],
               ['banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana',
                'banana']))  # 0
