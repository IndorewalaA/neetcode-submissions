class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to set to remove duplicates
        # iterate through set
        # if n - 1 not in set, check if next is in set, add consec streak
        if not nums:
            return 0
        nums_set = set(nums)
        max_count = 1
        for elem in nums_set:
            if (elem - 1) not in nums_set:
                count = 1
                while (elem + count in nums_set):
                    count += 1
                    max_count = max(max_count, count)
        return max_count