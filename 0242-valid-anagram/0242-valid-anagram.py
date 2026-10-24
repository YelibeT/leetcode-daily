class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        space complexity opt:
        """
        if len(s) > len(t):
            return False
        scount = Counter(s)
        print(scount)
        for char in t:
            if char not in s:
                return False
            else:
                scount[char] -= 1
        print(scount)
        for freq in scount.values():
            if freq != 0:
                return False
        return True