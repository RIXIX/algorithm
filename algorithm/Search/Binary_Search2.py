
# LEETCODE
# Arranging Coins
class Solution:
    def arrangeCoins(self, n: int) -> int:
        lst_num:int = 1
        lst:list = []
        
        if n==1:
            return 1
        for i in range(1,n+1):
            n -=i
            if n <0:
                return i-1


# 풀이 2
class Solution:
    def arrangeCoins(self, n: int) -> int:

        left = 0
        right = n

        while left <= right:
            middle = (left + right) // 2

            if (middle * (middle + 1)) / 2 < n:
                left = middle + 1
            elif (middle * (middle + 1)) / 2 > n:
                right = middle - 1
            else:
                return middle

        return right

# lesson learned
# 이진탐색, start + end / 2 = middle
# middle = n or 최종 right 값