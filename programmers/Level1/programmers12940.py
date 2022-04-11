def solution(n, m):
    max_div = 1
    min_mul = n * m
    n_divs = [i for i in range(1, n + 1) if n % i == 0]
    for n_div in n_divs:
        if m % n_div == 0 and n_div > max_div:
            max_div = n_div
            min_mul = int((m / max_div) * (n / max_div) * max_div)
    answer = [max_div, min_mul]
    return answer


print(solution(2, 5))
