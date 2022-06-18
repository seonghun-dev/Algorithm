def solution(d, budget):
    d.sort()
    budget_sum = 0
    for idx, val in enumerate(d):
        budget_sum += val
        if budget_sum > budget:
            return idx
    else:
        return len(d)