# BAEKJOON 9094
# Brute force


# for _ in range(T):
def oing (n, m):
    cnt = 0
    for i in range(1,n):
        for j in range(i+1, n):
            a = (i**2+j**2+m) / (i*j)
            # print(a)
            if a == int(a):
                cnt +=1
    return cnt          


T = int(input())

for _ in range(T):
    n, m = map(int ,input().split())
    print(oing(n,m))



# 다른사람풀이
def count_valid_pairs(n, m):
    count = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if (a**2 + b**2 + m) % (a * b) == 0: # 나눈 나머지가 0이라면, 정수
                count += 1
    return count

# 테스트 케이스 입력
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    result = count_valid_pairs(n, m)
    print(result)
