# Iterative BFS on a binary tree for level-order traversal

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Import dequeue
from collections import deque

class Solution:
    def bfs(self, root: TreeNode) -> list:
        if not root:
            return []
        
        result = []
        q = deque([root]) # The first level is simply the root, given that there is a root

        while q: # While the queue is not empty
            level_size = len(q)
            level = []

            for i in range(level_size):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) # For right to left order, simply append right before left
            
            result.append(level)
        
        return result

def build_tree(values):
    """
    Build a binary tree from a list (level-order).
    None entries mean missing nodes.
    """
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()

    return root

if __name__ == "__main__":
    sol = Solution()

    # Test 1: Empty tree
    root = build_tree([])
    assert sol.bfs(root) == []

    # Test 2: Single node
    root = build_tree([1])
    assert sol.bfs(root) == [
        [1]
    ]

    # Test 3: Perfect binary tree
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4  5  6   7
    root = build_tree([1,2,3,4,5,6,7])
    assert sol.bfs(root) == [
        [1],
        [2, 3],
        [4, 5, 6, 7]
    ]

    # Test 4: Left-skewed tree
    #   1
    #  /
    # 2
    #  /
    # 3
    root = build_tree([1,2,None,3])
    assert sol.bfs(root) == [
        [1],
        [2],
        [3]
    ]

    # Test 5: Right-skewed tree
    # 1
    #  \
    #   2
    #    \
    #     3
    root = build_tree([1,None,2,None,3])
    assert sol.bfs(root) == [
        [1],
        [2],
        [3]
    ]

    # Test 6: Mixed shape
    #       1
    #     /   \
    #    2     3
    #     \     \
    #      5     7
    root = build_tree([1,2,3,None,5,None,7])
    assert sol.bfs(root) == [
        [1],
        [2, 3],
        [5, 7]
    ]

    print("All BFS tests passed!")
