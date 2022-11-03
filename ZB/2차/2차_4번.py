def solution(delay, capacity, times):
    q_len = 0
    time = 0
    loss = 0
    for t in times:
        time += t
        while time >= delay:
            q_len -= 1
            time -= delay
        if q_len == capacity:
            loss += 1
            continue
        q_len += 1
    answer = loss
    return answer