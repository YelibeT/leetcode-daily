class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
    #move the right pointer the number is in the window
    #move the left pointer when the number is out of bounds shrink the window
    #track the servers that are active regardless of their freq
        logs.sort(key=lambda log: log[1])
        q = [[index, querie] for index, querie in enumerate(queries)]
        q.sort(key=lambda x:x[1])
        print(q)
        ans = [0] * len(queries)
        left = 0
        right = 0
        active = {}
        for idx, val in q:
            while right < len(logs) and logs[right][1] <= val:
                active[logs[right][0]] = active.get(logs[right][0], 0) + 1
                right += 1
            while left < right and logs[left][1] < val - x:
                active[logs[left][0]] -= 1
                if active[logs[left][0]] == 0:
                    active.pop(logs[left][0])
                left += 1
            ans[idx] = n - len(active)
        return ans