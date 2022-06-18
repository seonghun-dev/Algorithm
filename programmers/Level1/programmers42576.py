def solution(participant, completion):
    if result := list(set(participant) - set(completion)):
        return result[0]
    participant.sort()
    completion.sort()
    for idx, val in enumerate(participant):
        if completion[idx] != val:
            return val
