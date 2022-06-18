def solution(dartResult):
    answer_stack = []
    session_dic = {'S': 1, 'D': 2, 'T': 3}
    option_dic = {'#': -1, '*': 2}
    dartResult = dartResult.replace('10', 'x')
    for val in dartResult:
        if val in ['S', 'D', 'T']:
            answer_stack.append(answer_stack.pop() ** session_dic[val])
        elif val in ['#', '*']:
            current_val = answer_stack.pop() * option_dic[val]
            if answer_stack and val == '*':
                answer_stack.append(answer_stack.pop() * option_dic[val])
            answer_stack.append(current_val)
        else:
            answer_stack.append(int(val if val != 'x' else 10))
    return sum(answer_stack)


print(solution("1D2S#10S"))
