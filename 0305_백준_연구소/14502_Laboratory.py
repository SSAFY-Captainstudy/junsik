import sys
sys.stdin = open('sample.txt', 'r')

from collections import deque
def build_wall(cnt, total_size, array):
    if len(array) == 3:
        combination_index.append(array[:])
        return
    if cnt == total_size:
        return
    else:
        build_wall(cnt + 1, total_size, array)
        array.append(possible_wall[cnt])
        build_wall(cnt + 1, total_size, array)
        array.pop()

    

def spread_virus(temp_grid):
    q = deque(virus_list)
    while q:
        cur_i, cur_j = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = cur_i + di, cur_j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if temp_grid[ni][nj] == 0:
                    temp_grid[ni][nj] = 2
                    q.append((ni, nj))
    cnt = 0
    for r in range(N):
        for c in range(M):
            if temp_grid[r][c] == 0:
                cnt += 1
    return cnt

   
N, M = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]

max_v = 0
possible_wall = []
virus_list = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            possible_wall.append((i, j))
        elif grid[i][j] == 2:
            virus_list.append((i, j))

combination_index = []
build_wall(0, len(possible_wall), [])
for walls in combination_index:
    for di, dj in walls:
        grid[di][dj] = 1
    
    temp_grid = [row[:] for row in grid]
    max_v = max(max_v, spread_virus(temp_grid))

    for r, c in walls:
        grid[r][c] = 0
    

print(max_v)