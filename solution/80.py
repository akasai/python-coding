def solution(amount):
    coins = [100, 50, 10, 1]

    ans = []
    idx = 0
    while amount > 0:
        coin = coins[idx]
        if amount - coin < 0:
            idx += 1
            continue

        amount -= coin
        ans.append(coin)

    return ans


print(solution(123))
print(solution(350))
