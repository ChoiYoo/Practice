N = 3
trust = [[1, 3], [2, 3]]
def solution(N, trust):
    num_dict = {}
    x_list = []
    for x, y in trust:
        if y in num_dict:
            num_dict[y] += 1
        else:
            num_dict[y] = 1
        x_list.append(x)
    sorted_dict = sorted(num_dict.items(), key = lambda item: item[1], reverse = True)
    if sorted_dict[0][1] == N-1:
        p = sorted_dict[0][0]
        if p in x_list:
            answer = -1
        else:
            answer = p
    else:
        answer = -1

    return answer

print(solution(N, trust))