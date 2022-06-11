def solution(s):
    str_list = [ord(alpha) for alpha in s]
    str_list.sort(reverse=True)
    return ''.join([chr(ascii_val) for ascii_val in str_list])