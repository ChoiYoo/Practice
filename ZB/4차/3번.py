words = ["hello", "hear", "hell", "good", "goose", "children", "card", "teachable"]
queries = ["he??", "g???", "childre?", "goo????", "?"]

def solution(words, queries):
    answer = [[] for _ in range(len(queries))]
    for q in range(len(queries)):
        word = queries[q].split('?')[0]
        for w in words:
            if len(queries[q]) == len(w) and word == w[:len(word)]:
                answer[q].append(w)
    return answer

print(solution(words, queries))