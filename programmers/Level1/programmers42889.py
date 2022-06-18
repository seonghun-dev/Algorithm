from collections import Counter


def solution(N, stages):
    stages_count, stages = dict(Counter(stages)), [t for t in range(1, N + 1)]
    stages.sort(reverse=True)
    done = {}
    temp = stages_count[N + 1] if N + 1 in stages_count else 0
    for stage in stages:
        done[stage] = (stages_count[stage] if stage in stages_count else 0) + temp
        temp = done[stage]
    r = {t: (stages_count[t] / done[t] if t in stages_count and t in done else 0) for t in range(1, N + 1)}
    result = [t[0] for t in sorted(r.items(), key=lambda item: item[1], reverse=True)]
    return result


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
