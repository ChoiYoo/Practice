from collections import deque
start = [4, 2, 7, 2, 6]
time = [5, 2, 5, 4, 3]

def next(result, end):
    next = []
    for r in result:
        if r[0] <= end:
            next.append(r)
    next.sort(key=lambda x: (x[1], x[2], x[0]))
    return next[0]


def solution(start, time):
    answer = []
    result = deque()
    for i in range(len(start)):
        result.append([start[i], time[i], i])
    end = min(start)
    while result:
        r = next(result, end)
        end += r[1]
        answer.append(r[2])
        result.remove(r)
    return answer

print(solution(start, time))