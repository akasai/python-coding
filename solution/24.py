def solution(id_list, report, k):
    reported_map = {}
    report_map = {}

    for id in id_list:
        if id not in reported_map:
            reported_map[id] = set()
        if id not in report_map:
            report_map[id] = []

    for rp in report:
        r, a = rp.split(' ')
        reported_map[a].add(r)

    for rp in report:
        r, a = rp.split(' ')
        if len(reported_map[a]) >= k and a not in report_map[r]:
            report_map[r].append(a)

    ans = []
    for id in id_list:
        ans.append(len(report_map[id]))

    return ans


print(
    solution(['muzi', 'frodo', 'apeach', 'neo'], ['muzi frodo', 'apeach frodo', 'frodo neo', 'muzi neo', 'apeach muzi'],
             2))
print(solution(['con', 'ryan'], ['ryan con', 'ryan con', 'ryan con', 'ryan con'], 3))
