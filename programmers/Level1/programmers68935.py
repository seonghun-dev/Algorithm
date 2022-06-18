from itertools import combinations
solution = lambda n: sorted(list(set([sum(v) for v in list(combinations(n, 2))])))