class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        maxm = max(nums)
        ans = 0
        for num in nums:
            ans += (maxm - num)
        return ans
            