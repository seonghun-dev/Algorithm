solution = lambda arr, divisor: answer if (answer := sorted(filter(lambda x: x > 0, list(map(lambda x: x if x % divisor == 0 else 0, arr))))) else [-1]

print(solution([3, 2, 6], 10))
