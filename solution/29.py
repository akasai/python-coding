def solution(enroll, referral, seller, amount):
    tree_dic = dict(zip(enroll, referral))
    account_dic = {name: 0 for name in enroll}

    for i, s in enumerate(seller):
        money = amount[i] * 100
        curr = s
        while money > 0 and curr != '-':
            account_dic[curr] += money - money // 10
            money //= 10
            curr = tree_dic[curr]

    return [account_dic[name] for name in enroll]


# 360, 958, 108, 0, 450, 18, 180, 1080
print(solution(['john', 'mary', 'edward', 'sam', 'emily', 'jaimie', 'tod', 'young'],
               ['-', '-', 'mary', 'edward', 'mary', 'mary', 'jaimie', 'edward'],
               ['young', 'john', 'tod', 'emily', 'mary'],
               [12, 4, 2, 5, 10]))
# 0, 110, 378, 180, 270, 450, 0, 0
print(solution(['john', 'mary', 'edward', 'sam', 'emily', 'jaimie', 'tod', 'young'],
               ['-', '-', 'mary', 'edward', 'mary', 'mary', 'jaimie', 'edward'],
               ['sam', 'emily', 'jaimie', 'edward'],
               [2, 3, 5, 4]))
