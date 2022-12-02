nums = [2, 5, 10, 9, 8, 5]

def fastest_max_sum(nums):
    N = len(nums)
    answer = float('-inf')
    psum = 0
    for i in range(N):
        psum = max(psum, 0) + nums[i]
        answer = max(psum, answer)
    return answer

# def solution(nums):
#     answer = 0
#     result = []
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)+1):
#             n = nums[i:j]
#             result.append(sum(n) * min(n))
#     answer = max(result)
#     return answer

print(fastest_max_sum(nums))