class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        #binary search
        #find arr2 closest to arr1 and check the condition

        arr2.sort()
        cnt = 0
        for n1 in arr1:
            l = 0
            r = len(arr2) - 1
            valid = True
            while l <= r:
                m = l + (r-l) //2
                if abs(n1 - arr2[m]) <= d:
                    valid = False
                    break
                if arr2[m] < n1:
                    l = m + 1
                elif arr2[m] > n1:
                    r = m - 1
            if valid:
                cnt += 1
        return cnt
