titles = ["아모르파티", "아기상어", "올챙이와개구리", "산다는건"]
lyrics = ["산다는게다그런거지누구나빈손으로와...(후략)", "아기상어뚜루루뚜루귀여운뚜루루뚜루...(후략)", "개울가에올챙이한마리꼬물꼬물헤엄치다...(후략)", "산다는건다그런거래요힘들고아픈날도많지만...(후략)"]
problems = ["산다", "아기상어", "올챙이"]

def solution(titles, lyrics, problems):
    answer = [[] for _ in range(len(problems))]
    for p in range(len(problems)):
        for l in range(len(lyrics)):
            if problems[p] == lyrics[l][:len(problems[p])]:
                answer[p].append(titles[l])
    return answer

print(solution(titles, lyrics, problems))