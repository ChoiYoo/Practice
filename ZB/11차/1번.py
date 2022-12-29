def sort_count(num):
    s = ""
    for i in range(10):
        c = num.count(str(i))
        if c == 0:
            continue
        s = s + str(i) + str(c)
    return s
def solution(n, num):
    num = str(num)
    for _ in range(n):
        num = sort_count(num)
    return int(num)%10004

print(solution(n=3, num=5004223))