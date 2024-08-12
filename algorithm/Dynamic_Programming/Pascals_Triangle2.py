class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [comb(rowIndex, n) for n in range(rowIndex+1)]

# lesson learned
# 1. Pascals Triangle은 조합의 시각적 표현이다.
# 2. 1번과 다른 이유는, Index + 1에 대한 결과값 표출
 