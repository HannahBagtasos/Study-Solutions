# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        current = root
        while current:
            if val > current.val:
                current = current.right
            elif val < current.val:
                current = current.left
            else:
                return current  # Return the TreeNode itself
        return None  # Return None if the value is not found