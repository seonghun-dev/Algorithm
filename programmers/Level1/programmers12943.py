def solution(num):
    return answer if (answer := collatz(num) if num != 1 else 0) < 500 else -1


def collatz(num):
    return 1 if (num := num // 2 if num % 2 == 0 else 3 * num + 1) == 1 else collatz(num) + 1

print(solution(1))