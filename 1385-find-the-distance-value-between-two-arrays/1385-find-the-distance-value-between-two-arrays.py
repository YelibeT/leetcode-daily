class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for nums in arr1:
            for num in arr2:
                if abs(num - nums) <= d:
                    break
            else:
                count += 1
        return count
        