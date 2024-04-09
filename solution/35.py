def solution(n, words):
    mem = set()
    prev = words[0][0]
    for i, word in enumerate(words):
        if word in mem or (i > 0 and prev != word[0]):
            return [(i % n) + 1, i // n + 1]
        mem.add(word)
        prev = word[-1]
    return [0, 0]


print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))  # 3,3
print(solution(2, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))  # 3,3
print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))  # 1,3
print(solution(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']))  # 0,0
