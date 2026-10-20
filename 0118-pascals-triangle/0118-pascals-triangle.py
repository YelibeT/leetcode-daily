class Solution(object):
    def generate(self, numRows):
        """
        iterative row generation based on previous rows
        numRows- length of the triangle/rows to be generated
        """
        prevRow = [[1]]
        for i in range(numRows - 1):
            temp = [0] + prevRow[-1] + [0]
            
            nextRow = []
            for j in range(len(prevRow[-1]) + 1):
                #the next row is 1 + the prevRow
                nextRow.append(temp[j] + temp[j + 1])
            prevRow.append(nextRow)
        return prevRow

        
                


        