def solution(n, lost, reserve):
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
    last_lost_left = get_last_lost(-1, 2, lost, reserve)
    last_lost_right = get_last_lost(1, -2, lost, reserve)
    return n - min(last_lost_left, last_lost_right)


def get_last_lost(first, second, lost, reserve):
    lost = [l + first for l in lost]
    left_reserve = list(set(reserve) - set(lost))
    left_lost = list(set(lost) - set(reserve))
    if left_lost:
        last_lost = list(set([l + second for l in left_lost]) - set(left_reserve))
    else:
        last_lost = left_lost
    return len(last_lost)


print(solution(5, [1, 2, 4], [2, 3, 4, 5]))
