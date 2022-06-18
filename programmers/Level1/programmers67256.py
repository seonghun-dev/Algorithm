def solution(numbers, hand):
    hand = hand[0].upper()
    left_hand_loc = (3, 0)
    right_hand_loc = (3, 2)
    num_to_loc = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0),
                  5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1),
                  9: (2, 2), 0: (3, 1)}
    left = [1, 4, 7]
    right = [3, 6, 9]
    result = []
    for number in numbers:
        if number in left:
            result.append('L')
        elif number in right:
            result.append('R')
        else:
            left_distance = abs(num_to_loc[number][0] - left_hand_loc[0]) + abs(
                num_to_loc[number][1] - left_hand_loc[1])
            right_distance = abs(num_to_loc[number][0] - right_hand_loc[0]) + abs(
                num_to_loc[number][1] - right_hand_loc[1])
            if left_distance == right_distance:
                result.append(hand)
            elif left_distance < right_distance:
                result.append('L')
            elif left_distance > right_distance:
                result.append('R')
        if result[-1] == 'R':
            right_hand_loc = num_to_loc[number]
        else:
            left_hand_loc = num_to_loc[number]
    answer = ''.join(result)
    return answer


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
