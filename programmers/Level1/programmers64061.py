def solution(board, moves):
    pickup, result = [], 0
    for move in moves:
        for i in range(0, len(board)):
            if board[i][move - 1]:
                if pickup and pickup[-1] == board[i][move - 1]:
                    result += 2
                    pickup.pop()
                else:
                    pickup.append(board[i][move - 1])
                board[i][move - 1] = 0
                break
    return result
