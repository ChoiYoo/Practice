def solution(n):
    answer = []
    for i in range(1, n+1):
        answer.append(str(i))
    answer.sort()
    answer = list(map(int, answer))
    return answer

print(solution(n=15))

# 다 스트링으로 바꾼 후 lambda로 배열하기