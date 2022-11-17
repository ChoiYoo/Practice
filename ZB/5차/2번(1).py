numbers = [9, 5, 34, 3, 30]

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)

    return str(int(''.join(numbers)))

print(solution(numbers))