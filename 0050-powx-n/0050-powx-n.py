class Solution(object):
    def myPow(self, x, n):
        """
        how many time can we divide a num by 2-> log comp with base 2
        10-> 2^2 2^2 2^5
        dc
        x=0 return 0
        n=0 return 1
        """
        if x == 0: 
            return 0
        def recurse(x, n):
            if n == 0: 
                return 1
            res = recurse(x, n // 2)
            res *= res #the other half
            
            return x*res if n%2 else res #even and odd
        res = recurse(x, abs(n))
        if n<0: return 1/res
        return res
