class Solution(object):
    def setZeroes(self, matrix):
        rows = set()
        columns = set()

        # Step 2: Identify the rows and columns to be set to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        # Step 3: Set the entire row and column to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in columns:
                    matrix[i][j] = 0


# Instantiate the class and call the method
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

sol = Solution()
sol.setZeroes(matrix)
print(matrix)
