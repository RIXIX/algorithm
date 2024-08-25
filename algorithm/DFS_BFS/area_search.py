# BAEKJOON 2583

from collections import deque

def bfs(start_x, start_y, grid, M, N):
    # BFS를 수행하여 하나의 영역의 크기를 계산하는 함수
    # 시작점에서부터 인접한 모든 0 영역을 탐색합니다.
    queue = deque([(start_x, start_y)])
    grid[start_x][start_y] = 1  # 현재 위치를 방문 처리 (1로 설정)
    area_size = 0  # 현재 영역의 넓이를 저장하는 변수
    
    # 상하좌우 방향을 나타내는 벡터 (델타 배열)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        # 큐에서 현재 좌표를 꺼내고, 영역의 넓이를 증가시킵니다.
        x, y = queue.popleft()
        area_size += 1
        
        # 4방향(상하좌우)으로 탐색합니다.
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 새로운 좌표(nx, ny)가 그리드 내에 있고, 방문하지 않은 0인 경우
            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 0:
                grid[nx][ny] = 1  # 방문 처리
                queue.append((nx, ny))  # 큐에 새로 방문할 좌표 추가
    
    return area_size  # 현재 영역의 넓이를 반환

def find_areas(M, N, K, rectangles):
    # MxN 크기의 그리드를 0으로 초기화합니다.
    grid = [[0] * N for _ in range(M)]
    
    # 주어진 K개의 직사각형을 그리드에 그립니다.
    # 직사각형의 내부는 1로 채웁니다.
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        # (x1, y1)에서 (x2, y2)까지의 범위를 1로 채웁니다.
        for i in range(y1, y2):
            for j in range(x1, x2):
                grid[i][j] = 1
    
    areas = []  # 모든 분리된 영역의 넓이를 저장할 리스트
    
    # 그리드의 각 칸을 탐색하여 분리된 영역을 찾습니다.
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0:  # 직사각형 내부가 아니고, 방문하지 않은 곳이라면
                area_size = bfs(i, j, grid, M, N)  # BFS로 영역 크기 계산
                areas.append(area_size)  # 영역 크기를 리스트에 추가
    
    areas.sort()  # 영역 크기를 오름차순으로 정렬
    return len(areas), areas  # 분리된 영역의 개수와 각 영역의 넓이 리스트 반환

# 입력 처리
M, N, K = map(int, input().split())
rectangles = [tuple(map(int, input().split())) for _ in range(K)]

# 결과 계산
area_count, areas = find_areas(M, N, K, rectangles)

# 결과 출력
print(area_count)
print(' '.join(map(str, areas)))


# 입력 처리
M, N, K = map(int, input().split())
rectangles = [tuple(map(int, input().split())) for _ in range(K)]

# 결과 계산
area_count, areas = find_areas(M, N, K, rectangles)

# 결과 출력
print(area_count)
print(' '.join(map(str, areas)))



# 다른사람 풀이
import sys
sys.setrecursionlimit(10**6)  # 재귀 호출의 최대 깊이를 10^6으로 설정하여 RecursionError 방지

# M, N, K를 입력받습니다. M은 세로 길이, N은 가로 길이, K는 직사각형의 개수입니다.
m, n, k = map(int, input().split())

# M x N 크기의 그리드를 0으로 초기화합니다. 0은 비어있는 영역을 의미합니다.
graph = [[0] * n for _ in range(m)]

# K개의 직사각형의 좌표를 입력받아 그리드에 표시합니다.
# 직사각형의 내부는 1로 채웁니다.
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):  # y1부터 y2-1까지의 범위를 순회
        for j in range(x1, x2):  # x1부터 x2-1까지의 범위를 순회
            graph[i][j] = 1  # 직사각형 내부를 1로 채웁니다.

# 상하좌우 방향을 나타내는 델타 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 분리된 영역의 크기를 저장할 변수
count = 0

def dfs(x, y):
    """
    DFS를 사용하여 주어진 좌표 (x, y)에서 연결된 모든 영역을 탐색합니다.
    탐색한 영역의 넓이를 계산하여 반환합니다.
    """
    global count
    # 그리드 밖을 벗어나면 종료
    if x < 0 or x >= m or y < 0 or y >= n:
        return 0
    
    # 이미 방문했거나 직사각형 내부라면 종료
    if graph[x][y] == 1:
        return 0
    
    # 현재 위치를 방문했다고 표시 (1로 변경)
    graph[x][y] = 1
    count += 1  # 방문한 칸 수를 증가시킴
    
    # 상하좌우로 인접한 칸들을 재귀적으로 탐색
    for i in range(4):
        dfs(x + dx[i], y + dy[i])
    
    return count  # 현재 영역의 넓이를 반환

# 결과를 저장할 리스트
result = []

# 그리드의 모든 칸을 순회하며 DFS 탐색을 시작
for i in range(m):
    for j in range(n):
        # 현재 위치에서 DFS 탐색을 시작하여 새로운 영역을 찾으면
        cnt = dfs(i, j)
        if cnt:
            result.append(cnt)  # 탐색 결과를 리스트에 추가
            count = 0  # 다음 영역을 위해 count를 초기화

# 결과를 오름차순으로 정렬
result.sort()

# 분리된 영역의 개수를 출력
print(len(result))

# 각 영역의 넓이를 공백으로 구분하여 출력
for i in result:
    print(i, end=' ')
