from collections import deque

def solution(N, M, maze):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if maze[nx][ny] == 1:
                continue
            if maze[nx][ny] == 0:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    answer = maze[N-1][M-1]
    if answer == 0 or answer == 1:
        return -1
    else:
        return answer

print(solution(N=6, M=6, maze=[[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0], [1, 1, 1, 0, 0, 0]]))