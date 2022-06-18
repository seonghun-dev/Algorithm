import numpy as np


def solution(n, arr1, arr2):
    arr1 = [[int(k) for k in bin(r)[2:].zfill(n)] for r in arr1]
    arr2 = [[int(k) for k in bin(r)[2:].zfill(n)] for r in arr2]
    answer = (np.array(arr1) + np.array(arr2)).tolist()
    result = [''.join(['#' if col > 0 else ' ' for col in row]) for row in answer]
    return result

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
