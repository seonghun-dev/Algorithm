def solution(price, money, count):
    price_sum = 0
    for i in range(1, count + 1):
        price_sum += price * i
        if price_sum > money:
            price_sum += sum([price * k for k in range(i+1, count+1)])
            return price_sum - money
    else:
        return 0
print(solution(3,20,4))