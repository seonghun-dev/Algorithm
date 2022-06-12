from collections import Counter

import pandas as pd


def is_vip(period, payment_sum):
    if period >= 60:
        if payment_sum >= 600000:
            return True
        else:
            return False
    elif period >= 24:
        if payment_sum >= 900000:
            return True
        else:
            return False
    else:
        return False


def get_result(month1, month2):
    if not month1:
        if month2:
            return 1
        else:
            return 0
    elif not month2:
        if month1:
            return 2
        else:
            return 0
    else:
        return 0


def solution(periods, payments, estimates):
    df = pd.DataFrame({"periods": periods, "payments": payments, "estimates": estimates})
    df['recent_payment_sum'] = df['payments'].apply(lambda x: sum(x))
    df['estimate_payment'] = df.apply(lambda x: x['estimates'] + sum(x['payments'][1:]), axis=1)
    df['this_month_vip'] = df.apply(lambda x: is_vip(x['periods'], x['recent_payment_sum']), axis=1)
    df['next_month_vip'] = df.apply(lambda x: is_vip(x['periods'] + 1, x['estimate_payment']), axis=1)
    df['result'] = df.apply(lambda x: get_result(x['this_month_vip'], x['next_month_vip']), axis=1)
    return [Counter(df['result'])[1], Counter(df['result'])[2]]


solution([20, 23, 24],
         [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
          [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
          [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]],
         [100000, 100000, 100000])
solution([24, 59, 59, 60], [[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
                            [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
                            [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
                            [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]],
         [350000, 50000, 40000, 50000])
