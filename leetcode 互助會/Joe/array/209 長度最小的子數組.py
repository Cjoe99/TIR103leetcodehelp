class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        r,l = 0,0
        x_sum = 0
        max_l = len(nums)
        while r < max_l:
            x_sum += nums[r]
            while x_sum >= target:
                min_len = min(min_len,r-l+1)
                x_sum -= nums[l]
                l += 1
            r += 1
        return min_len if min_len != float('inf') else 0