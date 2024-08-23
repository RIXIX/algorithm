# Leetcode
# Problem : 
# 주어진 distance와 같거나 낮은 리프노드들의 Pair의 개수



class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        
        def dfs(node):
            if not node: # 노드가 비여있는 경우
                return []
            
            # 리프 노드일 경우
            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # left와 right 리스트의 모든 쌍에 대해 거리를 계산
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.result += 1
            
            # 부모 노드에 거리를 증가시켜 반환
            return [n + 1 for n in left + right]
        
        dfs(root)
        return self.result


# 정리 필요