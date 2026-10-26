class Solution(object):
    def canJump(self, nums):
        """
        
        we went with the array reversed

        """
        maxReach = 0 #maximum index the current index can reach 
        #if it can reach or pass the last index
        for i in range(len(nums) - 1):
            if i > 0 and nums[i - 1] == 0 and nums[i] != 0 and maxReach < i:
                return False
            maxReach = max(maxReach, i + nums[i])
            print(maxReach)
        return True if maxReach >= len(nums) - 1 else False
        