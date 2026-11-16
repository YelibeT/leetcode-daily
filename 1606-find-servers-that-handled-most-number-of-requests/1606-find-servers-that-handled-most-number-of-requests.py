class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        O(nlogk) + O(klogk) / O(k)
        """
        available = SortedList([i for i in range(k)])

        using = SortedList()
        res = [0] * k
        for i in range(len(arrival)):
            while using and using[0][0] <= arrival[i]:
                s = using.pop(0)[1] % k
                available.add(s)
            if available:
                idx = available.bisect_left(i % k)
                if idx == len(available):
                    idx = 0
                s = available.pop(idx)
                using.add((arrival[i] + load[i] , s))
                res[s] += 1
        maxm = max(res)
        ans = []
        for i in range(k):
            if res[i] == maxm:
                ans.append(i)
        return ans
        
        