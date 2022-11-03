from itertools import combinations
numbers = [0, 2, 4]
target = 12

def check(dict, result):
    for i in range(len(dict)):
        for j in dict[i+1]:
            if result == j:
                return i
    return -1

def solution(numbers, target):
    hap_list = {}
    for i in range(len(numbers)):
        c_list = combinations(numbers, i+1)
        hap_list[i+1] = []
        for c in c_list:
            hap_list[i+1].append(sum(c))
        hap_list[i+1].sort(reverse=True)
        for h in hap_list[i+1]:
            if h == 0:
                continue
            if target % h == 0:
                result = target // h
                c = check(hap_list, result)
                if c == -1:
                    answer = result * (i+1)
                    return answer
                else:
                    answer = c * (i+1)
                    return answer
    answer = -1
    return answer

print(solution(numbers, target))