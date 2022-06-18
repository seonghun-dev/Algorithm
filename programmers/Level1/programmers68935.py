def solution(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n, 3)
        answer += str(mod)
    return int(answer, 3)


print(solution(45))


def solution3(n):
    div, mod = divmod(n, 3)
    mod_list = [mod]
    while div != 1:
        div, mod = divmod(div, 3)
        mod_list.insert(0, mod)
    result = 0
    for idx, val in enumerate(mod_list):
        result += val * (3 ** (idx + 1))
    return result + 1


def ternary(x):
    div, mod = divmod(x, 3)
    return str(mod) + str(div) if div == 1 else str(mod) + ternary(div)


def solution2(n):
    return int(ternary(n), 3)
