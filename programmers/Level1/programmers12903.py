solution = lambda s: s[int(len(s) / 2): int(len(s) / 2) + 1 if len(s) % 2 == 1 else int(len(s) / 2) - 1: int(len(s) / 2) + 1]
print(solution("qwer"))