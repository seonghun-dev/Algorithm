def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"][(sum(month[0:a - 1]) + b) % 7]
