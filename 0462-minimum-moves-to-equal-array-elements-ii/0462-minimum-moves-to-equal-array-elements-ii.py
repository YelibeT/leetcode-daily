class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        #converge values to the middle value of the array
        nums.sort()
        middle = nums[len(nums) // 2]
        print(middle)
        ans = 0
        for num in nums:
            sub = abs(middle - num)
            print(sub)
            ans += sub
        return ans
