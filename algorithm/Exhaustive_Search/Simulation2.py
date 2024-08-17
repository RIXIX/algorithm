def solution(park, routes):
    start = []
    stop = []
    
    # 시작 위치와 장애물 위치 설정
    for i, j in enumerate(park):
        for q, w in enumerate(j):
            if w == 'S':
                start.append([i, q])
            if w == 'X':
                stop.append([i, q])
    
    start = sum(start, [])
    temp = [start.copy()]  # 처음 시작 위치를 기록

    # 이동 처리
    for r in routes:
        for _ in range(int(r[2])):
            if r[0] == "E" and [start[0], start[1] + 1] not in stop and start[1] + 1 <= int(q):
                start[1] += 1
            elif r[0] == "W" and [start[0], start[1] - 1] not in stop and start[1] - 1 >= 0:
                start[1] -= 1
            elif r[0] == "N" and [start[0] - 1, start[1]] not in stop and start[0] - 1 >= 0:
                start[0] -= 1
            elif r[0] == "S" and [start[0] + 1, start[1]] not in stop and start[0] + 1 <= int(i):
                start[0] += 1
            else:
                start = temp[-1].copy()  # 이동 실패 시 이전 위치로 복원
                break
        else:
            # 이동이 완료되면 현재 위치를 기록
            temp.append(start.copy())
    
    return start  # 최종 위치를 반환


# 풀이 2

def solution(park, routes):
    start = []
    stop = []
    
    # 공원의 크기
    n = len(park)       # 세로 길이
    m = len(park[0])    # 가로 길이
    
    # 시작 위치 및 장애물 위치 찾기
    for i, row in enumerate(park):
        for j, spot in enumerate(row):
            if spot == 'S':
                start = [i, j]
            if spot == 'X':
                stop.append([i, j])
    
    # 이동 명령 수행
    for route in routes:
        direction, steps = route.split()
        steps = int(steps)
        
        temp = start.copy()  # 이동 이전 위치 저장 
        for _ in range(steps):
            if direction == "E" and start[1] + 1 < m and [start[0], start[1] + 1] not in stop:
                start[1] += 1
            elif direction == "W" and start[1] - 1 >= 0 and [start[0], start[1] - 1] not in stop:
                start[1] -= 1
            elif direction == "N" and start[0] - 1 >= 0 and [start[0] - 1, start[1]] not in stop:
                start[0] -= 1
            elif direction == "S" and start[0] + 1 < n and [start[0] + 1, start[1]] not in stop:
                start[0] += 1
            else:
                start = temp  # 이동 불가 시 이전 위치로 복구
                break

    return start


# lesson learned 
# !! copy를 통해서 값을 구해야 하는 방식 start.copy()
# [start[0], start[1] + 1]   이런식으로, 리스트 원소 별 합 구하는 방식
# 배열을 구할때는 len을 참고
# direction, steps = route.split()에 대한 방식
# 