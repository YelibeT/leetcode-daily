class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        space complexity opt:
        """
        if len(s) > len(t):
            return False
        sset = set(s)
        for char in t:
            if char not in sset or s.count(char) != t.count(char):
                return False
        return True
        