import pandas as pd


def split_plan(plans, add_service=False):
    data, service = [], []
    for plan in plans:
        plan_split = plan.split(' ')
        plan_split = list(map(int, plan_split))
        data.append(plan_split[0])
        service.append(plan_split[1:] + service[-1] if service and add_service else plan_split[1:])
    return data, service


def find_plan(plan_df, data, service):
    plan_df = plan_df[plan_df['data'] >= data]
    plan_df = plan_df[plan_df['service'].apply(lambda x: all(y in x for y in service))]
    if plan_df.empty:
        return 0
    else:
        return plan_df['plan'].min()


def solution(n, plans, clients):
    data, service = split_plan(plans, add_service=True)
    plan_df = pd.DataFrame({'data': data, 'service': service, 'plan': range(1, len(data) + 1)})
    data, service = split_plan(clients)
    client_df = pd.DataFrame({'data': data, 'service': service})
    client_df['plan'] = client_df.apply(lambda x: find_plan(plan_df, x['data'], x['service']), axis=1)
    answer = client_df['plan'].tolist()
    return answer


print(solution(5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"]))
print(solution(4, ["38 2 3", "394 1 4"], ["10 2 3", "300 1 2 3 4", "500 1"]))
