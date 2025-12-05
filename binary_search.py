class Solution:
    def search(self, nums: list, target: int) -> int:
        """
        nums: sorted list of integers
        target: target integer
        This function will return the index of target if target is in nums
        Otherwise, will return -1
        """

        l, r = 0, len(nums) - 1

        while(l <= r): # when pointers cross, exit

            m = (l+r)//2 # alternatively, use l + [(r - l) // 2]

            if nums[m] > target: # if the middle pointer is too big, only look to the left
                r = m - 1

            elif nums[m] < target: # if the middle pointer is too small, only look to the right
                l = m + 1

            else: # the only other possibility is if the middle pointer equals the target
                return m # in which case the current index should be returned
            
        # the while loop only exits once the pointers cross
        # the pointers cross iff target is not in nums
        # thus, return -1
        return -1
    
if __name__ == "__main__":
    sol = Solution()

    assert sol.search([1, 2, 3, 4, 5], 3) == 2
    assert sol.search([1, 2, 3, 4, 5], 6) == -1
    assert sol.search([-5, -3, 0, 4, 9], 4) == 3
    assert sol.search([2], 2) == 0
    assert sol.search([], 7) == -1

    print("All tests passed!")
