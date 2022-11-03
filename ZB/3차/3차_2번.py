delay = 0
N = 5
def solution(delay, N):
    n_list = [1]
    hap = 0
    a = 1
    b = 1 + delay
    if delay == 0:
        for f in range(N+1):
            hap += 2**f
    for _ in range(delay + 1):
        n_list.append(2)
    for d in range(delay-1):
        n_list.append(2 * (d+2))
    if N <= delay + 1:
        hap = sum(n_list[0:N+1])
    else:
        for _ in range(N-(delay+1)):
            next_num = sum(n_list[a:b+1])
            a += 1
            b += 1
            n_list.append(next_num)
        hap = sum(n_list[0:N+1])
    answer = hap
    return answer

print(solution(delay, N))