class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return true if any value appears more than once
        # else false

        # turn into a set?
        count = len(nums)
        nums = set(nums)
        if len(nums) != count:
            return True
        return False
