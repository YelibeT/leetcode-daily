class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()

        unavail = []
        avail = [i for i in range(n)]
        count = [0] * n

        for s, e in meetings:
            while unavail and s >= unavail[0][0]:
                end, room = heapq.heappop(unavail)
                heapq.heappush(avail, room)

            if len(avail) == 0:
                end_time, room = heapq.heappop(unavail)
                duration = e - s
                e = end_time + duration
                heapq.heappush(avail, room)
            
            room = heapq.heappop(avail)
            heapq.heappush(unavail, (e, room))
            count[room] += 1
        maxm = max(count)
        print(count)
        for i in range(len(count)):
            if count[i] == maxm:
                return i