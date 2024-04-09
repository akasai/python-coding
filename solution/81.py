def solution(items, weight_limit):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0
    remain_weight = weight_limit

    for w, v in items:
        if w <= remain_weight:
            remain_weight -= w
            total_value += v
        else:
            frac = remain_weight / w
            total_value += (v * frac)
            break

    return total_value


print(solution([[10, 19], [7, 10], [6, 10]], 15))
print(solution([[10, 60], [20, 100], [30, 120]], 50))
