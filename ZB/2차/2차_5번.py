from copy import deepcopy

def change(i, j, K, image):
    result = 0
    for x in range(K):
        for y in range(K):
            if i+x < 0 or i+x >= len(image) or j+y <0 or j+y >= len(image[0]):
                plus = 0
            else:
                plus = image[i+x][j+y]
            result += plus
    result = result // (K*K)
    return result

def solution(image, K):
    answer = deepcopy(image)
    for i in range(len(image)):
        for j in range(len(image[0])):
            answer[i][j] = change(i-(K//2), j-(K//2), K, image)

    return answer