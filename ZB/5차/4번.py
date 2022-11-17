from copy import deepcopy

N = 10
branches = [6, 7, 10, 16, 12]

def devide(a, b):
    return a//b

def solution(N, branches):
    b = sum(branches)
    n = b // N
    while True:
        new_b = deepcopy(branches)
        for i in range(len(branches)):
            new_b[i] = new_b[i] // n
        if sum(new_b) >= N:
            break
        else:
            n -= 1

    return n

print(solution(N, branches))