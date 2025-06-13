n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# 2 theives, 2 dfs calls.

# We need a value computation function
# Go through the first dfs looping through all the rows.
# If the first theif was chosen,
# Check overlap
# Call the second dfs for the second theif and choose
# Compute value and update through dfs



from itertools import combinations

def compute_segment(combination):

    best = 0
    for i in range(1, m+1):
        for elem in combinations(combination, i):
            local_best = sum(elem)

            if local_best <= c:
                cur_value = sum(comp*comp for comp in elem)
                best = max(best, cur_value)
    return best


# We need a row to compute values, maybe loop later

# We have all possible theif combinations
segments = []
for r in range(n):
    target_row = weight[r]

    for start in range(len(target_row) - m + 1):
        combination = target_row[start : start + m]
        value = compute_segment(combination)
        segments.append((r, start, value))

# Okay, now I can compute values since dfs computes all of the values first,



best_value = 0
chosen = []

def dfs(theif, used_segment, total_value):

    global best_value

    # Terminal condition, when we choose all the two theives, we stop.
    if theif == 2:
        best_value = max(best_value, total_value)
        return 

    # We check every segment, from inside here, we call every other components and compare the results
    for i in range(len(segments)):

        row, start, value = segments[i]

        # if we have overlap
        overlap = False
        for used_row, used_start, _ in used_segment:
            if used_row == row and abs(start - used_start) < m:
                overlap = True
                break
            # After break, we did the dfs(2nd_theif) so we go straight to the pop()
        
        if not overlap:
            used_segment.append((row, start, value))
            dfs(theif + 1, used_segment, total_value + value)
            # When the above dfs breaks, the above dfs is terminated, so we go beneath.
            used_segment.pop()

dfs(0, [], 0)
print(best_value)






    




