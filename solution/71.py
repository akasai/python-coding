def solution(nums):
    N = len(nums)
    dp = [1] * N

    for i in range(1, N):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
            print(dp)

    return max(dp)


print(solution([1, 4, 2, 3, 1, 5, 7, 3]))
print(solution([3, 2, 1]))
