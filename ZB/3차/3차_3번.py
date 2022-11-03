import math
from collections import deque

reward = [29, 40, 99, 0, 5, 5]
health = [50, 60, 100, 100, 100, 100]
optional = [1, 1, 1, 0, 0, 0]

def solution(reward, health, optional):
    zero_list = []
    one_list = deque()
    for i in range(len(optional)):
        if optional[i] == 0:
            zero_list.append(i)
        else:
            one_list.append(i)
    min_num = float('INF')
    while True:
        time, h = 0, 1
        for i in range(len(zero_list)):
            time += math.ceil(health[zero_list[i]] / h)
            h += reward[zero_list[i]]
        if min_num < time:
            break
        elif one_list == deque():
            break
        else:
            min_num = time
            zero_list.append(one_list.popleft())
            zero_list.sort()
    answer = min_num
    return answer

print(solution(reward, health, optional))