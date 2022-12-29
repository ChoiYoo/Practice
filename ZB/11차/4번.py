
def solution(money, chips):
    memo = [None for _ in range(money+1)]
    memo[0] = 0

    def dp(change):
        for total in range(1, change+1):
            min_num = total
            for chip in chips:
                if total >= chip:
                    result = memo[total - chip]
                    min_num = min(result, min_num)
            memo[total] = min_num + 1
        return memo[change]
    return dp(money)

print(solution(money=3000, chips=[1100, 500, 200, 150, 25]))