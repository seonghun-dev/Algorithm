solution = lambda left, right: sum([-i if (i ** (1 / 2)).is_integer() else i for i in range(left, right + 1)])