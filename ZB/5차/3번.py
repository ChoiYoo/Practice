arr = [-3, 0, 3, 4, 5, 12, 15, 14, 12, 11]



def solution(arr):
    answer = -1
    new = []
    for a in range(len(arr)):
        new.append([arr[a], a])
    max_num = max(new)
    if max_num[1] != 0 and max_num[1] != len(arr)-1:
        answer = max_num[1]
    return answer

print(solution(arr))