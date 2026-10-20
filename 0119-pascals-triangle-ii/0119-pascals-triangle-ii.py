class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prevRow = [[1]]
        for i in range(rowIndex):
            temp = [0] + prevRow[-1] + [0]
            nextRow = []
            for j in range(len(prevRow[-1]) + 1):
                #the next row is 1 + the prevRow
                nextRow.append(temp[j] + temp[j + 1])
            prevRow.append(nextRow)
        return prevRow[-1]
        