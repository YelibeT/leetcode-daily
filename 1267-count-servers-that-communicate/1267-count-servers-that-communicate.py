class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        communicable_servers_count = 0

        for row_index in range(rows):
            row_counts = 0
            server_column_index = -1

            for col_index in range(cols):
                if grid[row_index][col_index] == 1:
                    if row_counts == 0:
                        server_column_index = col_index
                    row_counts += 1

            can_communicate = (row_counts != 1)
            if not can_communicate:
                for i in range(rows):
                    if i != row_index and grid[i][server_column_index] == 1:
                        can_communicate = True
                        break
            if can_communicate:
                communicable_servers_count += row_counts

        return communicable_servers_count