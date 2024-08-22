def count_bad_grass_islands(R, C, grid):
    # 방향 벡터: 상, 하, 좌, 우, 대각선 (총 8 방향)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    def dfs(r, c):
        stack = [(r, c)]
        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] > 0:
                    visited[nx][ny] = True # 위아래좌우대각선 탐색 및 인접점 True
                    stack.append((nx, ny))

    visited = [[False] * C for _ in range(R)]
    island_count = 0

    for i in range(R):
        for j in range(C):
            # 1이상의 섬 발견 시
            if grid[i][j] > 0 and not visited[i][j]: #인접점 or 0 제외 전체 탐색
                # 새 섬 발견
                visited[i][j] = True
                dfs(i, j) # 인접점 전부 체크 True/False
                island_count += 1

    return island_count

# 입력 처리

import sys
sys.stdin = open ("in1.txt", "r")
# input = sys.stdin.read
# data = input().split()
# print(data)

R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
# print(grid)
# data = sum(data, [])

# 결과 출력
print(count_bad_grass_islands(R, C, grid))
