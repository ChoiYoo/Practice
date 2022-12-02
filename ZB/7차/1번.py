img = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

def solution(img):
    answer = ''
    num = img[0][0]
    check_num = [[num]*len(img) for _ in range(len(img))]
    if img == check_num:
        return str(num)
    answer += '('
    for a in range(4):
        result = slicecheck(img, a)
        if result == '0' or result == '1':
            answer += result
        else:
            answer += (solution(result))
    answer += ')'
    return answer

def slicecheck(img, x):
    new_img = []
    l = len(img) // 2
    zero_list = [[0]*l for _ in range(l)]
    one_list = [[1]*l for _ in range(l)]
    if x == 0:
        for i in range(l):
            new_img.append(img[i][:l])
    elif x == 1:
        for i in range(l):
            new_img.append(img[i][l:])
    elif x == 2:
        for i in range(l):
            new_img.append(img[i+l][:l])
    else:
        for i in range(l):
            new_img.append(img[i+l][l:])

    if new_img == zero_list:
        return '0'
    elif new_img == one_list:
        return '1'
    else:
        return new_img

print(solution(img))