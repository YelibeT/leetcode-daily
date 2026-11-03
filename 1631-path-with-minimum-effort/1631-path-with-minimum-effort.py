class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        """

        start => 0,0 and destination=> row - 1, col - 1
        [(0,2),(0,2),(0,2),(1,2),(3,2)] maxm = 3
        [(2,3),(2,5),(2,3),(2,5)] maxm = 2 


        """

        minHeap = [[0,0,0]]
        visit = set()
        drn = [[0,1], [1,0], [0,-1],[-1,0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r,c) in visit:
                continue
            visit.add((r,c))
            if (r,c) == (len(heights) - 1, len(heights[0]) - 1):
                return diff
            
            for dr, dc in drn:
                newR, newC = r + dr, c + dc

                if (newR < 0 or newC < 0 or newR == len(heights) or newC == len(heights[0]) or (newR, newC) in visit):
                    continue
                maxDiff = max(diff, abs(heights[newR][newC] - heights[r][c]))

                heapq.heappush(minHeap, [maxDiff, newR,newC])
        