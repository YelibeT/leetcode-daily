class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            anotherS = ""
            for i in range(len(s)):
                if s[i] == "0":
                    anotherS += "1"
                else:
                    anotherS += "0"
            return anotherS
        #there is no guarantee that ans will be built till k because the thing increases exponentially
        #so can't return ans[-1] because thats not where k is
        def recurse(curr):
            if len(curr) >= k:
                return curr
            inverted = invert(curr)
            return recurse(curr + "1" + inverted[::-1])

        ans = recurse("0")
        print(ans)

        return ans[k-1]