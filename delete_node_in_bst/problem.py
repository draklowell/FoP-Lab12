# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSmallest(self, root: TreeNode) -> TreeNode:
        while root.left is not None:
            root = root.left

        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        if root.right is None:
            return root.left

        if root.left is None:
            return root.right

        smallest = self.findSmallest(root.right)
        smallest.left = root.left
        return root.right
