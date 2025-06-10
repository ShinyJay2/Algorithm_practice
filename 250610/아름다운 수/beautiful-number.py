n = int(input())

# We need to print answers, how many of them?

answer = []

def print_ans():
    print(len(answer))


# We need the recursive function, what is the terminal condition?
# cur_num is our current number

def beautiful(cur_num):

    if len(cur_num) == n:
        answer.append(cur_num)
        return 

    for i in range(1, 5):
        if len(cur_num) + i <= n:
            beautiful(cur_num + str(i) * i)

beautiful("")
print_ans()
