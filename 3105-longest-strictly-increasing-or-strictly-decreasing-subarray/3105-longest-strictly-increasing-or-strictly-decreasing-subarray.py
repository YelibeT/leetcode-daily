class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = 1
        decreasing = 1
        maxm = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing += 1
                decreasing = 1
            if nums[i] < nums[i - 1]:
                decreasing += 1
                increasing = 1
            if nums[i] == nums[i - 1]:
                decreasing = 1
                increasing = 1
            maxm = max(increasing, decreasing, maxm)
        return maxm