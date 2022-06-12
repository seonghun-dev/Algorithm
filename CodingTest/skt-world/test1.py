def solution(p):
    change_count = [0 for _ in range(len(p))]
    for i, v in enumerate(p):
        r = min(p[i:])
        r_idx = p.index(r)
        if r < p[i]:
            change_count[i] += 1
            change_count[r_idx] += 1
            p[i], p[r_idx] = r, p[i]
    return change_count


print(solution([2, 5, 3, 1, 4]))
