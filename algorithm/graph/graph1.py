# 문제 Leetcode 1791. Find Center of Star Graph
# edge 구조 [[1,2,3],[1,4,5][2,1,8]]
# center = 1
# return 1
# 풀이 1 리스트 컴프리헨션
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return [x for x in edges[0] if all(x in lst for lst in edges)][0]

# 풀이 2 reduct를 통한 해결
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return list(reduce(lambda x, y : set(x)&set(y), edges))[0]

# 풀이 3 교집합 사용
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return list(set(edges[0]).intersection(*edges[1:]))[0]



# lesson learned
# 1번 풀이
# all() = True 인 x의 값으로 값을 구할 수 있음.
# [i for ~ if True/False ] 구조

# 2번 풀이
# reduct 함수는 iterable한 첫번쨰, 두번째 요소를 function에 전달하여 연산을 수행함.
# lambda x, y : 첫번쨰, 두번째 요소를 set(x)&set(y)를 통해 교집합으로 연산하여 수행
# ex) [[1,2,3],[1,4,5][2,6,8]]
# x: [1,2,3] / y : [1,4,5] = 1
# x: 1 / y :[2,1,8]  = 1
# return 1

# 3번 풀이
# set().intersection()을 통해 교집합 생성
# set([1,2,3]).intersection(*[][][])
# *를 넣는 이유는 []를 순차적으로 여러개를 넣어야 할때, 개별 리스트로 전달해야 할떄
# 각 개별 리스트의 교집합을 구한다.