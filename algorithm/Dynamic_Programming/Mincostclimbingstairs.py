class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n == 0:
            return 0
        elif n == 1:
            return cost[0]
        
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        
        return min(dp[n-1], dp[n-2])




# 다른사람 풀이
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        if n == 0:
            return 0
        elif n == 1:
            return cost[0]
        
        # Initialize the first two steps
        prev2 = cost[0]
        prev1 = cost[1]
        
        # Iterate through the cost array
        for i in range(2, n):
            curr = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, curr
        
        # The result is the minimum cost of either stepping from the last or second-last step
        return min(prev1, prev2)



        