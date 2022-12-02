s = "2552552551"

def solution(s):
    answer = []
    for x in range(1,4):
        if x >= len(s) - 2:
            break
        for y in range(x+1, x+4):
            if y >= len(s)-1:
                break
            for z in range(y+1, y+4):
                result = ''
                if z >= len(s):
                    break
                if check(s, x, y, z):
                    result = s[:x] + '.' + s[x:y] + '.' + s[y:z] + '.' + s[z:]
                    answer.append(result)
    return answer

def check(s, x, y, z):
    first = s[:x]
    second = s[x:y]
    thrid = s[y:z]
    fourth = s[z:]

    if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0') or (len(thrid) > 1 and thrid[0] == '0') or (len(fourth) > 1 and fourth[0] == '0'):
        return False
    elif 0 <= int(first) <= 255 and 0 <= int(second) <= 255 and 0 <= int(thrid) <= 255 and 0 <= int(fourth) <= 255:
        return True
    else:
        return False

print(solution(s))