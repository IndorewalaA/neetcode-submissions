class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return true if any value appears more than once
        # else false

        # turn into a set?
        nums_set = set(nums)
        if len(nums) != len(nums_set):
            return True
        return False
