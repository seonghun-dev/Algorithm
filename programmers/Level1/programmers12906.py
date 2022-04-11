def solution(arr):
    answer = []
    for val in arr:
        if answer:
            if answer[-1] != val:
                answer.append(val)
        else:
            answer.append(val)
    return answer


arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))
