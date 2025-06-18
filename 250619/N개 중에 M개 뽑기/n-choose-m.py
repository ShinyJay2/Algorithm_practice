N, M = map(int, input().split())

from itertools import combinations

num_list = [i for i in range(1, N+1)]

result = []

for comb in combinations(num_list, M):
    result.append(comb)
    print(comb[0], comb[1])


