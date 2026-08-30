class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums -> ints
        # target -> int
        # ret i and j such that nums @ i and j == target
        # idea: create a dict that pairs nums to indices
        # iterate through list, if target - curr is in list, index of it
        num_dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in num_dict:
                return [num_dict[target - nums[i]], i]
            num_dict[nums[i]] = i