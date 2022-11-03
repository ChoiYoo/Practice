def change(num_list):
    result = 0
    zero = 0
    for i in range(len(num_list)-1, -1, -1):
        result += 10**zero * num_list[i]
        zero += 1
    return result

def solution(a, b):
    a = change(a)
    b = change(b)
    ab = a + b
    answer = list(map(int, str(ab)))
    return answer