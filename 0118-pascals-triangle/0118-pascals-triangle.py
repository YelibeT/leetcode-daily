class Solution(object):
    def generate(self, numRows):
        """
        


        """
        res = [[1]]
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]#add 0s at the start and end
            row = []
            for j in range(len(res[-1]) + 1):#the next row is in the length of the previous row
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res
                


        