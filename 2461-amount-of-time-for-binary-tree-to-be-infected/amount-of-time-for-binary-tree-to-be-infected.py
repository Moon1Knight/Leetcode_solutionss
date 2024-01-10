class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
      def dfs(node):
        if not node: 
          return 0, 0, 0, 0

        dl, scl, sll, tl = dfs(node.left)
        dr, scr, slr, tr = dfs(node.right)

        depth = max(dl, dr) + 1
        if node.val == start:
          return depth, 1, depth, depth -1
        else:
          if scl != 0:
            return depth, scl+1, sll, max(tl, scl + dr, sll - 1)
          elif scr != 0:
            return depth, scr+1, slr, max(tr, scr + dl, slr - 1)
          else:
            return depth,0,0,0

      return dfs(root)[3]