def solution(s, n):
    result = []
    for i in s:
        v = ord(i) + n if i.isalpha() else ord(i)
        result.append(chr(v - 26 if (v > 122 and ord(i) > 97) or (v > 90 and 91 > ord(i)) else v))
    return ''.join(result)
print(solution('AaZz ',25))