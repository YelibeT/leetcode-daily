class Solution(object):
    def canJump(self, nums):
        """
        
        we went with the array reversed

        the zero-check Can you refactor the logic to remove the special zero-check and rely solely on updating the max reach?

        """
        maxReach = 0 #maximum index the current index can reach 
        #if it can reach or pass the last index
        for i in range(len(nums) - 1):
            if i > maxReach: #we are at an index that maxReach didnot reach or pass
                return False
            maxReach = max(maxReach, i + nums[i])
            print(maxReach)
        return True if maxReach >= len(nums) - 1 else False
        