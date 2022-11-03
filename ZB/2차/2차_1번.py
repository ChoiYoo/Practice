def solution(numbers):
    numbers.sort()
    start_num = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] != start_num + 1:
            answer = start_num + 1
            break
        else:
            start_num += 1
    return answer