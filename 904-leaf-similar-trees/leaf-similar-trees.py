# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def get_leaf_sequence(node, sequence=None):
            if sequence is None:
                sequence = []

            if not node.left and not node.right:
                sequence.append(node.val)
            else:
                if node.left:
                    get_leaf_sequence(node.left, sequence)
                if node.right:
                    get_leaf_sequence(node.right, sequence)

            return sequence

        sequence1 = get_leaf_sequence(root1)
        sequence2 = get_leaf_sequence(root2)

        return sequence1 == sequence2