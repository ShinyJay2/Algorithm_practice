n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# I have no absolutely no idea.
# The ladder is descending, so maybe sort by height.
edges.sort(key = lambda x: x[1])


# m is the number of lines, so we need a height, which is the max of the second element of edges.
height = edges[-1][1]


def descend_ladder(given_edges):
    # Since we already ordered this by height, we only need 1d arr
    ladder = [i for i in range(1, n+1)]

    # Descending the ladder is just swapping coord_x
    for coord_x, _ in given_edges:
        ladder[coord_x - 1], ladder[coord_x] = ladder[coord_x], ladder[coord_x - 1]

    return ladder

def compare(ladder1, ladder2):
    if ladder1 != ladder2:
        return False
    return True


target = descend_ladder(edges)

ans = m+1

# let's do dfs. How? 
def dfs(lines, given_edges):

    global ans

    if len(given_edges) >= ans:
        return

    # Used up all the lines
    if lines == m:
        if compare(descend_ladder(given_edges), target):
            ans = min(ans, len(given_edges))
        return

    # edges is a list, so given_edges must be a list also.
    dfs(lines + 1, given_edges + [edges[lines]])

    dfs(lines + 1, given_edges)

    return

dfs(0, [])
print(ans)