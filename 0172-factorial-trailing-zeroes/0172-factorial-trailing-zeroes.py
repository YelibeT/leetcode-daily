class Solution(object):
    def trailingZeroes(self, n):
        """

        factorial
        digit

        to know if there are trailing zeroes:
        if we find a 5 in the expansion of n! there is a zero 

        the number of 0s in the end of n! = the number of 5s in the expansion of n!-> mulptiples of 5 arent counted as ones

        x/5 + x/5^2+...

        trailing zeroes requires a factor of 10-> 5*2

        time comp: log(n)
        """
        
        def factorial(n, count):
            if n == 0:
                return count
            n //= 5
            count += n
            return factorial(n, count)
        return factorial(n, 0)