class Solution:
    def minMoves(self, nums: list[int]) -> int:
        subtracts = 0
        #when length == 2?
        #its okay we work on n - 1 elements till they equal the last
        minm = min(nums)
        for i in range(len(nums)):
            sub = nums[i] - minm
            subtracts += sub
        return subtracts
