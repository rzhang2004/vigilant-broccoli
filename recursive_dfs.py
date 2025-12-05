# Recursive DFS on a binary tree

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Implementing DFS
class Solution:
    def dfs(self, root: TreeNode) -> int:
        if not root: # if root.left or root.right returns None, then this will call
            return 0 # the depth of a nonexistent child is 0
        
        return 1 + max(self.dfs(root.left), self.dfs(root.right))
    

# test cases

if __name__ == "__main__":
    sol = Solution()

    # Test 1: Empty tree
    root = None
    assert sol.dfs(root) == 0

    # Test 2: Single node
    root = TreeNode(1)
    assert sol.dfs(root) == 1

    # Test 3: Perfect balanced tree (depth = 3)
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4  5  6   7
    root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7))
    )
    assert sol.dfs(root) == 3

    # Test 4: Left-skewed tree (depth = 4)
    #    1
    #   /
    #  2
    # /
    #3
    #/
    #4
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert sol.dfs(root) == 4

    # Test 5: Right-skewed tree (depth = 3)
    # 1
    #  \
    #   2
    #    \
    #     3
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert sol.dfs(root) == 3

    # Test 6: Uneven tree (depth = 4)
    #        1
    #      /   \
    #     2     3
    #    /
    #   4
    #  /
    # 5
    root = TreeNode(1,
        TreeNode(2, TreeNode(4, TreeNode(5))),
        TreeNode(3)
    )
    assert sol.dfs(root) == 4

    # Test 7: Missing children (depth = 3)
    #     1
    #    / \
    #   2   3
    #    \
    #     4
    root = TreeNode(1,
        TreeNode(2, None, TreeNode(4)),
        TreeNode(3)
    )
    assert sol.dfs(root) == 3

    print("All tests passed!")
