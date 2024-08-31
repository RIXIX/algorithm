class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        
        dp = [0]*(n+1)
        dp[1]=1
        dp[2]=1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            # print(i , dp[i])
        return dp[n]




# 다른사람 풀이
class Solution:
    def tribonacci(self, n: int) -> int:
        d = [0,1,1]
        for i in range(3, n+1):
            d.append(d[i-1] + d[i-2] + d[i-3])

        return d[n]