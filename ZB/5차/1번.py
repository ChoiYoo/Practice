from collections import Counter

s = "imfinethankyou"
t = "atfhinemnoyuki"

def solution(s, t):
    if s is None or t is None or len(s) != len(t):
        return False

    return True if sorted(s) == sorted(t) else False

# def solution(s, t):
#     answer = True
#     s = list(s)
#     s.sort()
#     t = list(t)
#     t.sort()
#     if s == t:
#         answer = True
#     else:
#         answer = False
#     return answer

print(solution(s, t))