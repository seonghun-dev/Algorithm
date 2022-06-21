import numpy as np

def solution(A, B):
    A.sort(), B.sort(reverse=True)
    return int(np.dot(np.array(A), np.array(B)))
