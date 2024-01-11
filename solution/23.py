def solution(genres, plays):
    music_map = {}
    count = {}

    for i in range(len(genres)):
        if genres[i] not in music_map:
            music_map[genres[i]] = []
        music_map[genres[i]].append((i, plays[i]))
        count[genres[i]] = count.get(genres[i], 0) + plays[i]

    count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    ans = []
    for k, _ in count:
        music_map[k].sort(key=lambda x: (-x[1], x[0]))
        ans.extend([idx for idx, _ in music_map[k][:2]])

    return ans


print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))  # 4,1,3,0
