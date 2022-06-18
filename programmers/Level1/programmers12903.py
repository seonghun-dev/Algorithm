def solution(s):
    div, mod = divmod(len(s), 2)
    return s[div-1] + s[div] if mod == 0 else s[div]