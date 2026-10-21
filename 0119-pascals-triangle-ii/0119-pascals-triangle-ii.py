class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]

        prevRow = self.getRow(rowIndex - 1)

        temp = [0] + prevRow + [0]
        nextRow = []

        for j in range(len(prevRow) + 1):
            nextRow.append(temp[j] + temp[j + 1])

        return nextRow
        