n = int(input())
A = list(map(int, input().split()))

total_final = float("inf")

for i in range(n):

    length_list = []
    total = 0

    for j in range(n):
        length = abs(j - i)
        length_list.append(length)

    for people, length in zip(A, length_list):
        total += people * length

    total_final = min(total, total_final)

print(total_final)



    


