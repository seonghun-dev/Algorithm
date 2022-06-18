import math
from itertools import combinations


def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = len([r for comb in list(combinations(nums, 3)) if primenumber(r := sum(comb))])
    return answer
