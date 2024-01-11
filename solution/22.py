def solution(record):
    text = []
    name_dic = {}
    for r in record:
        arr = r.split(' ')

        if r.startswith('enter'):
            name_dic[arr[1]] = arr[2]
            text.append((arr[1], '님이 들어왔습니다.'))
        elif r.startswith('leave'):
            text.append((arr[1], '님이 나갔습니다.'))
        elif r.startswith('change'):
            name_dic[arr[1]] = arr[2]

    ans = []
    for (k, v) in text:
        ans.append(name_dic[k] + v)
    return ans


def other_solution(record):
    text = []
    name_dic = {}
    for r in record:
        arr = r.split(' ')
        if arr[0] != 'leave':
            name_dic[arr[1]] = arr[2]

    for r in record:
        arr = r.split(' ')
        if arr[0] == 'enter':
            text.append('%s님이 들어왔습니다.' % name_dic[arr[1]])
        elif arr[0] == 'leave':
            text.append('%s님이 나갔습니다.' % name_dic[arr[1]])

    return text


# print(solution(
#     ['enter uid1234 muzi', 'enter uid4567 prodo', 'leave uid1234', 'enter uid1234 prodo', 'change uid4567 ryan']))
print(other_solution(
    ['enter uid1234 muzi', 'enter uid4567 prodo', 'leave uid1234', 'enter uid1234 prodo', 'change uid4567 ryan']))
