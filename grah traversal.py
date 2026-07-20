from collections import deque

def bfs(grid, row, col, rows, cols):
    queue = deque()

    queue.append((row, col))
    grid[row][col] = 0

    while queue:
        current_row, current_col = queue.popleft()

        
        up = current_row - 1
        if up >= 0:
            if grid[up][current_col] == 1:
                queue.append((up, current_col))
                grid[up][current_col] = 0

        
        down = current_row + 1
        if down < rows:
            if grid[down][current_col] == 1:
                queue.append((down, current_col))
                grid[down][current_col] = 0

        
        left = current_col - 1
        if left >= 0:
            if grid[current_row][left] == 1:
                queue.append((current_row, left))
                grid[current_row][left] = 0

        
        right = current_col + 1
        if right < cols:
            if grid[current_row][right] == 1:
                queue.append((current_row, right))
                grid[current_row][right] = 0


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter the matrix row wise:")

for i in range(rows):

    while True:

        row = list(map(int, input(f"Row {i + 1}: ").split()))

        if len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            continue

        valid = True

        for value in row:
            if value != 0 and value != 1:
                valid = False
                break

        if not valid:
            print("Only 0 and 1 are allowed.")
            continue

        break

    grid.append(row)

islands = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:
            islands += 1
            bfs(grid, i, j, rows, cols)

print("\nTotal Number of Islands =", islands)
