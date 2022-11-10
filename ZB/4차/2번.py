words = ["hello", "hell", "good", "goose", "children", "card", "teachable"]
queries = ["hell*", "goo*", "*able", "qua*"]

def solution(words, queries):
    answer = []
    for q in queries:
        cnt = 0
        for w in words:
            if q[0] == '*' and q[1:] == w[len(w)-(len(q)-1):]:
                cnt += 1
            if q[len(q)-1] == '*' and q[:len(q)-1] == w[:len(q)-1]:
                cnt += 1
        answer.append(cnt)
    return answer

print(solution(words, queries))