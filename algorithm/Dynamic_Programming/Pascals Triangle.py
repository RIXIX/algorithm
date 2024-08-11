class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []

        for i in range(num_Rows):
            rows = [1] * (i+1)

            for j in range(1, i):
                rows[j]=lst[i-1][j-1] + lst[i-1][j]
            
            lst.append(rows)
        
        return lst



# 풀이 2
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return [[comb(n,x) for x in range(n+1)] for n in range(numRows)]



# lesson learned
# 1. Pascals Triangle은 조합의 시각적 표현이다.
# 2. 리스트 컴프리헨션(List Comprehension) [[x for ~] for ~] 이 가능하다.
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = [n for n in numbers if n % 2 == 0]
# print(even_numbers)  # 출력: [2, 4, 6]
