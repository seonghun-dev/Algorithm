"""
강  : 0
숲 : 1
평지 : 2
"""


def solution(grid, k):
    change_dict = {'.': 0, 'F': 1, '#': 2}
    grid = [[change_dict[t] for t in v] for v in grid]
    sleep_time = 0
    m, n = len(grid), len(grid[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = []
    stack = []
    stack.append((0, 0))
    walk = 0
    while stack:
        walk += 1
        x, y = stack.pop()
        if (x, y) not in visited:
            visited.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if grid[nx][ny] == 2:
                continue
            if grid[nx][ny] == 1:
                grid[nx][ny] = grid[x][y] + 1
                stack.append((nx, ny))
            if grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1
                stack.append((nx, ny))
    sleep_time = int(grid[m - 1][n - 1] / k)
    return sleep_time


print(solution(["..FF", "###F", "###."], 4))
print(solution(["..FF", "###F", "###."], 5))
print(solution(
    [".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.",
     ".#...####F", "...#......"], 6))
