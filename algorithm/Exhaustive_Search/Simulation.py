# 프로그래머스
# 바탕화면 정리

def solution(wallpaper):
    res = [1]
    res = [1]*4
    w = []
    v = []
    for index, lst in enumerate(wallpaper):
        if '#' in lst:
            w.append(index)
            v.append(list(filter(lambda x : lst[x] == '#', range(len(lst)))))
    v = sum(v, [])
    v.sort()
    res[0] = w[0]
    res[2] = w[-1]+1
    res[1] = v[0]
    res[3] = v[-1]+1
    
    return res

# result [#이 존재하는 가장 작은 index, 전체 #의 가장 왼쪽, #이 존재하는 가장 맨 마지막 리스트의 index+1,  
# 전체 #의 가장 오른쪽 index+1]


# lesson learned
# enumerate로, index 확인가능
# lst(filter(lambda x: lst[x] == 'condition', range(len(lst)))))
# lst는 string으로 literable하므로 '#'이 어디있는지 '..#' 라는 문자열에서 filter로 찾아서 찾아서 해당 index 추가
# v = sum(v, [])라는 표현으로 [[]] 이중 리스트를 [] 1차원 리스트로 차원 축소
# v를 정렬하여, 1차원 리스트 내, X위치를 파악하여 추가



# 다른사람풀이 2

def solution(wallpaper):
    a, b = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]