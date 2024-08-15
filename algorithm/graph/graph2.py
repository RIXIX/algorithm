# LEETCODE 1971. Find if Path Exists in Graph

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # 그래프를 인접 리스트로 표현
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # DFS 탐색
        stack = [start]
        visited = set()

        while stack:
            node = stack.pop()
            if node == end:
                return True
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    stack.append(neighbor)

        return False


# lesson learned
# graph {} 컴프리 헨션 적용 가능 
# graph = {i for i in range(n)}

# 아래처럼, 연결되어 있는 node 확인할 수 있음.
#for a, b in edges:
#    graph[b].append(a)
#    graph[a].append(b)

# node = stack.pop() 하면, node에는 pop된 수가 지정되며, stack에는 그 수가 빠진 값의 리스트로 존재
# ex) stack = [1,2,3] stack.pop()-> node = 3 , stack = [1,2]
# 