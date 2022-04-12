import numpy as np


def solution(arr1, arr2):
    array1 = np.array(arr1)
    array2 = np.array(arr2)
    np_answer = array1 + array2
    answer = np_answer.tolist()
    return answer
