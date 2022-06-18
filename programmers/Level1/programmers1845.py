from collections import Counter


def solution(nums):
    num, collection = int(len(nums) / 2), len(dict(Counter(nums)))
    return collection if collection <= num else num


print(solution([3, 1, 2, 3]))
