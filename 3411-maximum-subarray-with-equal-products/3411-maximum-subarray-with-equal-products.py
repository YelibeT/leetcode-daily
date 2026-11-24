class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            prod = nums[i]
            gcds = nums[i]
            lcms = nums[i]
            for j in range(i + 1, len(nums)):
                prod = prod * nums[j]
                gcds = gcd(gcds, nums[j])
                lcms = lcm(lcms, nums[j])
                if prod > gcds * lcms:
                    break
                if prod == gcds * lcms:
                    res = max(res, j - i + 1)
        return res