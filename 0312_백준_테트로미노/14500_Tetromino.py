import sys
sys.stdin = open('sample.txt', 'r')

def make_tetromino(array, cur_sum):
    global max_v
    if len(array) == 4:
        if max_v < cur_sum:
            max_v = cur_sum
        return
    
    if len(array) == 3:
        cur_i, cur_j = array[1]
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = cur_i + di, cur_j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj]:
                    visited[ni][nj] = 1
                    make_tetromino(array + [(ni, nj)], cur_sum + grid[ni][nj])
                    visited[ni][nj] = 0



    cur_i, cur_j = array[-1]
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = cur_i + di, cur_j + dj
        if 0 <= ni < N and 0 <= nj < M:
            if not visited[ni][nj]:
                visited[ni][nj] = 1
                make_tetromino(array + [(ni, nj)], cur_sum + grid[ni][nj])
                visited[ni][nj] = 0

N, M = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_v = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        make_tetromino([(i, j)], grid[i][j])
        visited[i][j] = 0
print(max_v)