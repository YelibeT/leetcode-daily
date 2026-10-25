class Solution(object):
    def myPow(self, x, n):
        """
        x^n -> x^(n//2)
        4-> 2
        100000000000000000000000/2
        10000000000/2

        """
        if x == 0:
            return 0
        def recurse(x, n):
            if n == 0:
                return 1
            res = recurse(x, n//2)
            #return multiply
            res = res * res
            return x * res if n % 2 else res
        ans = recurse(x, abs(n))
        if n < 0:
            return 1/ans
        return ans