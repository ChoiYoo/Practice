buildings = [[1, 8, 4], [2, 4, 10], [3, 5, 6], [10, 12, 6]]

def find(buildings):
    max_num = 0
    for b in buildings:
        max_num = max(max_num, b[1])
    return max_num

def solution(buildings):
    answer = []
    max_num = find(buildings)
    building = [0]*(max_num + 2)
    for i in buildings:
        for j in range(i[0], i[1]):
            building[j+1] = max(building[j+1], i[2])

    for b in range(1, max_num+2):
        if building[b] != building[b-1]:
            answer.append([b-1, building[b]])

    return answer

print(solution(buildings))