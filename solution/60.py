def solution(s):
    s = s[2:-2].split('},{')
    s = sorted(s, key=len)

    ans = []
    for elmt in s:
        e_lst = elmt.split(',')
        for e in e_lst:
            if e not in ans:
                ans.append(e)
    return [int(a) for a in ans]


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # 2134
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # 2134
print(solution("{{20,111},{111}}")) # 111,20
print(solution("{{123}}")) # 123
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # 2341
