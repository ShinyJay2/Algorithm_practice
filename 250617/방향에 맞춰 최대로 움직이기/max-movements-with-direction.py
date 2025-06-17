n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# initial thinking:
# we need param of: location (tuple), and score of how many times we can move
# What is the base case? When we cannot move we terminate?
# We need a move function, defining when given location tuple and direction, moves the cur_pos into new_pos, maybe use dx dy technique
# Maybe terminal condition can be achieved by the move function

# Maybe call the dfs(row, col, move+1)
# If we cannot move more and we cannot call the next dfs, pop that move and backtrack?

command = dict()
move_list = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
for i in range(1, 9):
    command[i] = move_list[i-1]

# nx, ny = x + dx, y + dy

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# Given x, y, coord, we have to move

# We will return possible positions
def move(x, y):

    possible = []
    # Check in range of the grid, and keep the possible move positions
    cur_move_dir = move_dir[x][y]
    dx, dy = command[cur_move_dir]
    for i in range(1, n):
        nx, ny = x +  i * dx, y + i * dy
        if not in_range(nx, ny):
            break
        if num[x][y] < num[nx][ny]:
            possible.append((nx, ny))

    return possible

# We need to recurse by all possible coordinates. for example with the second example, we start at 5, search till the end when we visit 6, and backtrack, and search till the end when we visit 7
# dfs terminal condition would be when we search for all possible locations, so in order for the next step, we need the next coordinates, and the idx, or recurse depth

best = 0

def dfs(x, y, idx):

    global best

    # This is the terminal condition
    if not move(x, y):
        best = max(best, idx)
        return

    # We need to call the next dfs
    for nx, ny in move(x, y):
        dfs(nx, ny, idx+1)

dfs(r-1, c-1, 0)

print(best)






