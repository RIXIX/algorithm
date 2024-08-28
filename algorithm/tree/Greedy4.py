# LEETCODE
# 409. Longest Palindrome
#  
from collections import Counter


# from collections import Counter
# 딕셔너리구조로 알파벗 종류별 개수로 나타남

class Solution:
    def longestPalindrome(self, s):
        # 문자 빈도 계산
        freq = Counter(s)
        
        length = 0
        odd_found = False
        
        for count in freq.values():
            # 짝수는 모두 더할 수 있다
            if count % 2 == 0:
                length += count
            else:
                # 홀수는 하나는 중앙에 배치하고, 나머지는 짝수로 만든다
                length += count - 1
                odd_found = True
        
        # 홀수가 하나라도 있다면 중앙에 배치할 수 있으므로 길이에 1을 더한다
        if odd_found:
            length += 1
        
        return length



# 다른사람 풀이
class Solution:
    def longestPalindrome(self, s: str) -> int:

        res=odd=0

        for key, val in Counter(s).items():
            res +=val -odd if val % 2 else val # 홀수면 val-odd 짝수면 val
            odd=1 if val % 2 else odd # 홀수면 odd=1 짝수면 odd=0
        return res
