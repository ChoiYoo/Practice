from collections import deque

nums = "14152944"

def solution(nums):
    answer = []
    first = len(nums) // 3
    second = (len(nums) - first) // 2
    for i in range(1, first+1):
        for j in range(i+1, i+second+1):
            answer = check(nums, i, j)
            if answer != False:
                return answer
    return {}

def check(nums, i, j):
    answer = []
    if (len(nums[:i]) > 1 and nums[:i][0] == '0') or (len(nums[i:j]) > 1 and nums[i:j][0] == '0'):
        return False
    f = int(nums[:i])
    s = int(nums[i:j])
    n = deque(nums[j:])
    answer.append(f)
    answer.append(s)
    while n:
        compare_num = ''
        for _ in range(len(str(f+s))):
            compare_num += n.popleft()
        compare_num = int(compare_num)
        if compare_num == f+s:
            answer.append(compare_num)
            f, s = s, compare_num
        else:
            return False
    return answer

print(solution(nums))