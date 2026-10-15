class Solution(object):
    def jump(self, nums):
        """

        we need to know to which position will the current position take us
        if i + nums[i] >= len(nums) - 1:
            step = 1 
        
        so comes level by level exploration - bfs
        """
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
        
            

        