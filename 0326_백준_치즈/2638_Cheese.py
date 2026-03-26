import sys
sys.stdin = open('sample.txt', 'r')

from collections import deque
def check_hole():
    q = deque()
    q.append((0,0))
    while q:
        cur_r, cur_c = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = cur_r + di, cur_c + dj
            if 0 <= ni < N and 0 <= nj < M:
                if grid[ni][nj] == 0 and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = 1


N, M = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]

t = 0
cnt = 0
result = []

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            cnt += 1
            
while cnt > 0:
    result.append(cnt)
    edge = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    check_hole()
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1:
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ni, nj = r + di, c + dj
                        if 0 <= ni < N and 0 <= nj < M:
                            if visited[ni][nj] == 1:
                                edge[r][c] += 1
    cur_cnt = 0
    for r in range(N):
        for c in range(M):
            if edge[r][c] >= 2:
                grid[r][c] = 0
            if grid[r][c] == 1:
                cur_cnt += 1
    
    cnt = cur_cnt
    t += 1
    
print(t)
