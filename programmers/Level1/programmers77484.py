def solution(lottos, win_nums):
    min, undefine = len(list(set(win_nums) - set(lottos))), lottos.count(0)
    return [1 + min - undefine if 1 + min - undefine + 1 < 7 else 6, 1 + min if min + 1 < 7 else 6]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
