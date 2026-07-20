from collections import deque

def bfs(grid, row, col, rows, cols):
    queue = deque()

    
    queue.append((row, col))

    grid[row][col] = 0

    while queue:
        current_row, current_col = queue.popleft()

       
        if current_row - 1 >= 0 and grid[current_row - 1][current_col] == 1:
            queue.append((current_row - 1, current_col))
            grid[current_row - 1][current_col] = 0


        if current_row + 1 < rows and grid[current_row + 1][current_col] == 1:
            queue.append((current_row + 1, current_col))
            grid[current_row + 1][current_col] = 0

        
        if current_col - 1 >= 0 and grid[current_row][current_col - 1] == 1:
            queue.append((current_row, current_col - 1))
            grid[current_row][current_col - 1] = 0

        
        if current_col + 1 < cols and grid[current_row][current_col + 1] == 1:
            queue.append((current_row, current_col + 1))
            grid[current_row][current_col + 1] = 0



rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter the matrix row wise:")

for i in range(rows):
    row = list(map(int, input(f"Row {i + 1}: ").split()))

    while len(row) != cols:
        print(f"Please enter exactly {cols} values.")
        row = list(map(int, input(f"Row {i + 1}: ").split()))

    grid.append(row)

islands = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:
            islands += 1
            bfs(grid, i, j, rows, cols)

print("\nTotal Number of Islands =", islands)
