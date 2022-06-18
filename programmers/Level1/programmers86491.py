def solution(sizes):
    sizes = [[max(size), min(size)] for size in sizes]
    result = max([i[0] for i in sizes]) * max([i[1] for i in sizes])
    return result


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
