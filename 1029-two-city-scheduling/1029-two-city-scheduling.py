class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        
        """
        costs.sort(key=lambda cost: cost[0] - cost[1])
        minCost = 0
        for i in range(len(costs)):
            if i < len(costs) // 2:
                minCost += costs[i][0]
            else:
                minCost += costs[i][1]
        return minCost
        