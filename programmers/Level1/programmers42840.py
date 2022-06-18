def solution(answers):
    answer_len = len(answers)
    sheet = [sum([[1, 2, 3, 4, 5] for _ in range(int(answer_len / 5 + 1))], [])[:answer_len],
             sum([[2, 1, 2, 3, 2, 4, 2, 5] for _ in range(int(answer_len / 8 + 1))], [])[:answer_len],
             sum([[3, 3, 1, 1, 2, 2, 4, 4, 5, 5] for _ in range(int(answer_len / 10 + 1))], [])[:answer_len]]
    score = [0, 0, 0]
    for idx, val in enumerate(answers):
        for i, v in enumerate(score):
            score[i] += 1 if (sheet[i][idx] == val) else 0
    return [i + 1 for i, v in enumerate(score) if v == max(score)]


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
