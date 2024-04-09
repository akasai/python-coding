def solution(arr1, arr2):
    merge = []
    l, r = 0, 0
    while l < len(arr1) and r < len(arr2):
        if arr1[l] < arr2[r]:
            merge.append(arr1[l])
            l += 1
        else:
            merge.append(arr2[r])
            r += 1
    while l < len(arr1):
        merge.append(arr1[l])
        l += 1
    while r < len(arr2):
        merge.append(arr2[r])
        r += 1

    return merge


print(solution([1, 3, 5], [2, 4, 6]))
print(solution([1, 2, 3], [4, 5, 6]))
