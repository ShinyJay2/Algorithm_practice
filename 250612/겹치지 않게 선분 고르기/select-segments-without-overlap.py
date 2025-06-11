n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# First we get the line coordinates in tuples
# Then we sort them by their starting point. What has the earliest starting point?

lines = []
for c1, c2 in zip(x1, x2):
    lines.append((c1, c2))

lines.sort(key = lambda x: x[0])

# Now we explore using dfs
# We need to keep the max

max_line_count = 0

def dfs(line_idx, last_coord, line_count):

    global max_line_count

    # What is the terminal condition of dfs?
    # We should run out of lines.

    if line_idx == n:
        max_line_count = max(max_line_count, line_count)
        return 

    # What is the internal content of the dfs?
    # If lines do not overlap, we call the dfs
    # If overlap, we skip that line. How do we skip? We just call the next dfs with the current line_end (How do you think like this? Hard af)

    if lines[line_idx][0] > last_coord:
        dfs(line_idx + 1, lines[line_idx][1], line_count + 1)

    dfs(line_idx + 1, last_coord, line_count)

    return

dfs(0, -100, 0)
print(max_line_count)