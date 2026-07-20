from collections import deque


def bfs(grid, row, col, rows, cols):
    queue = deque()
    queue.append((row, col))


    grid[row][col] = 0

    while queue:
        current_r, current_c = queue.popleft()

       
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            new_r = current_r + dr
            new_c = current_c + dc

            
            if (0 <= new_r < rows and
                0 <= new_c < cols and
                grid[new_r][new_c] == 1):

                queue.append((new_r, new_c))
                grid[new_r][new_c] = 0 



rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter the matrix values row wise (only 0 and 1):")


for i in range(rows):
    row = list(map(int, input(f"Row {i + 1}: ").split()))

    
    while len(row) != cols or any(value not in (0, 1) for value in row):
        print(f"Please enter exactly {cols} values using only 0 and 1.")
        row = list(map(int, input(f"Row {i + 1}: ").split()))

    grid.append(row)


islands = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:
            islands += 1
            bfs(grid, i, j, rows, cols)


print("number of islands:", islands)