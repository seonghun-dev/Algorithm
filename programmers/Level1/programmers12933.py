def solution(n):
    answer = list(map(int, str(n)))
    answer.sort(reverse=True)
    answer=int(''.join(map(str, answer)))
    return answer