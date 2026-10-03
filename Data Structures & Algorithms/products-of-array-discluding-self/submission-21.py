class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if 0 present
        prod = 1
        ans = []
        has_0 = False
        for num in nums:
            if num != 0:
                prod *= num
            else:
                if has_0:
                    ans = [0] * len(nums)
                    return ans
                has_0 = True
        for num in nums:
            if has_0:
                if num == 0:
                    ans.append(prod)
                else:
                    ans.append(0)
            else:
                ans.append(int(prod / num))
        return ans

                
        
            