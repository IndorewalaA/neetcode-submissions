class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return true if any value appears more than once
        # else false

        # turn into a set?
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False