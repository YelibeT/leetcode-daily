import math
class Solution(object):
    def countGoodNumbers(self, n):
        """

        at even index-> even
        odd index-> prime

        4
        02345678
        5^11 5^2^5
        """      
        MOD = 10**9 + 7
        odd = n // 2
        even = n - odd
        print(even)
        print(odd)
        def pow(x, n):
            if n == 0: 
                return 1
            res = pow(x, n // 2)
            res = (res * res) % MOD #the other half
                
            return x*res if n%2 else res #even and odd
                
        return (pow(5, even) * pow(4, odd)) % MOD