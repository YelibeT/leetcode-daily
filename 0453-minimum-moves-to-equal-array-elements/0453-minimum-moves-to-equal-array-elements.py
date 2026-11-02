class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        subtracts = 0
        if len(nums) == 1:
            return subtracts
        #when length == 2?
        #its okay we work on n - 1 elements till they equal the last
        
        minm = min(nums)
        for i in range(len(nums)):
            sub = nums[i] - minm
            subtracts += sub
        return subtracts
