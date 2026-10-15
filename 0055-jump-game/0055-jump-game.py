class Solution(object):
    def canJump(self, nums):
        """

        bt - o(2n)
        dp - o(n2)?
        greedy - o(n)

        issues: trying every possible jump
        reaching False after doing almost n steps
        repeated work
        fixes: check if one position can reach the next or pass it
        catch Falses early
        no need to check every possible jump just check if the least can make it 

        """
        goalPost = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goalPost:
                #it can reach so update the goal for the next
                goalPost = i
        return True if goalPost == 0 else False

        
        
                
            
            
            
            

            
        