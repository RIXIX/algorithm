# BAEKJOON 1145
# 적어도 대부분의 배수

def search(nums):
    num = 1
    while True:

        count = sum(num % x == 0 for x in nums)
        if count >= 3:
            return num
        num +=1

nums = list(map(int, input().split()))

# print(search(nums))


def search2(nums):
    n = 1
    while True:
        cnt = 0
        for i in nums:
            if n%i == 0:
                cnt+=1
            if cnt >=3:
                return n
        n+=1

nums = list(map(int, input().split()))

print(search2(nums))


