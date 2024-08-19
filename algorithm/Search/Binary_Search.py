class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lst_len = len(nums)
        lst_set = [x for x in range(lst_len+1)]
        find_value = [i for i in lst_set if i not in nums]

        return find_value[0]



# 풀이 2
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # initialize missing_num to n
        missing_num = len(nums)
        
        # loop through the array nums
        for i, num in enumerate(nums):
            # perform XOR operation with index and element
            missing_num ^= i ^ num
        
        # return the missing number
        return missing_num


# lesson learned
# missing_num ^= i ^ num  == missing_num = missing_num ^ i ^ num
# XOR 연산지 = '^' : 
# XOR 연산의 교환 법칙과 결합 법칙에 의해, 어떤 순서로 숫자와 인덱스를 XOR하더라도 결과는 동일
# 최종적으로 missing_num에는 빠진 숫자만 남게 됩니다.
# [3, 0 , 1]
# 3 ^ 0 ^ 3 = 0
# 0 ^ 1 ^ 0 = 1
# 1 ^ 2 ^ 1 = 2

# [3, 2, 1, 0]
# 4 ^ 0 ^ 3 = 7
# 7 ^ 1 ^ 2 = 4
# 4 ^ 2 ^ 1 = 7
# 7(0111) ^ 3(0011) = (0100) ^ 0(0000) = 4(0100)
# XOR(배타적 논리합) 연산자는 비트 연산의 하나
# 개념 : 두비트가 다를 때만 '1'을 반환하고 같을떄는 '0'을 반환하는 연산