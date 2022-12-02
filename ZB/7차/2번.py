votes = [1, 4, 2, 2, 2, 3, 2, 2, 1]

def solution(votes):
    answer = 0
    goal_num = (len(votes) // 2)
    while True:
        answer += 1
        if votes.count(answer) > goal_num:
            break
    return answer

print(solution(votes))