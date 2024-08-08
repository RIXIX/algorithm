# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        dummy = TreeNode(-1)  # 임시 노드
        current = dummy
        
        for value in inorder(root):
            current.right = TreeNode(value)
            current = current.right
        
        return dummy.right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
        
        dummy = TreeNode(-1)  # 임시 노드
        current = dummy
        
        inorder(root)

        for value in res:
            current.right = TreeNode(value)
            current = current.right
        
        return dummy.right