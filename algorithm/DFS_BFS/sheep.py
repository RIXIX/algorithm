# COUNTING SHEEP
# BAEKJOON 11123
# https://www.acmicpc.net/problem/11123

def bfs(grid, visited, start, H, W):
    queue = [start]
    visited[start[0]][start[1]] = True
    
    # 상하좌우 방향만 탐색
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_sheep_groups(grid, H, W):
    visited = [[False] * W for _ in range(H)]
    sheep_groups = 0
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visited[i][j]:
                bfs(grid, visited, (i, j), H, W)
                sheep_groups += 1
    
    return sheep_groups

# 입력 처리
T = int(input())  # 테스트 케이스의 수

for _ in range(T):
    H, W = map(int, input().split())
    grid = [input().strip() for _ in range(H)]
    print(count_sheep_groups(grid, H, W))


# 다른사람 풀이
# (https://ye5ni.tistory.com/177)
import sys
sys.setrecursionlimit(100000)
 
T = int(input())        # 입력 받을 테스트 케이스의 수
 
""" dfs 알고리즘 사용 하기 """
def dfs(y, x):
    graph[y][x] = '.'   # 이미 방문한 곳은 '.' 으로 표시
    dy = [0,1,0,-1]     # 상하좌우로 탐방할 좌표값 설정
    dx = [1,0,-1,0]
    for k in range(4):      # 상하좌우에 '#'이 있는지
        ny = y + dy[k]
        nx = x + dx[k]
        if ny >= 0 and nx >= 0 and ny < H and nx < W:   # 지정 범위를 벗어 나지 않는 선에서 확인 하기
            if graph[ny][nx] == '#':    # '#'을 발견했으면 다시 그 자리에서 재귀 호출
                dfs(ny, nx)
 
for _ in range(T):
    H,W = map(int, input().split())     # 그리드의 높이(H)와 너비(W) 입력받기
    graph = [list(input()) for _ in range(H)]   # 양과 풀의 그리드 정보를 저장할 수 있는 공간 설정
    count = 0   # 몇 개의 양 무리가 있는지 카운트 할 변수
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#':  # 양이 발견 됐을 경우
                dfs(i, j)
                count += 1  # 하나의 무리 발견 (카운트 추가)
 
    print(count)