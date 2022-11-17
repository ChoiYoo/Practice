N, M, fry, clean = 4, 20, [2, 2, 1, 3], [2, 4, 3, 2]

def check(n, time):
    c = []
    for t in time:
        if n % t == 0:
            c.append(n)
    if c == []:
        return False
    else:
        return c

def solution(N, M, fry, clean):
    answer = 0
    time = []
    total = []
    for i in range(N):
        time.append(fry[i] + clean[i])
    min_num = min(time)
    for i in range(min_num, max(time) * (M//N + 1)):
        if check(i, time) != False:
            total += check(i, time)
    max_time = total[M-2]
    for t in range(M-3, 0):
        if max_time > total[t]:
            max_time = total[t]
            break
    min_time = float('INF')
    f = 0
    for i in range(N):
        com = (max_time // time[i]) * time[i]
        if min_time > com:
            min_time = com
            f = fry[i]
    return min_time + f

print(solution(N, M, fry, clean))