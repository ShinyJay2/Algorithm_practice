K, N = map(int, input().split())

# First, I need an array to store the temporary combinations

answer = []

def print_ans():
    for elem in answer:
        print(elem, end=" ")
    print()

# Second, I need a function that defines the nth number, in this case, 1 or 2.

def choose_k(n):

    # What did you learn so far? We must define the terminal condition first.
    # Always the terminal condition first when recursive function.

    # So the terminal condition should be, when we reach the depth of the tree, in this case, 2, we should never reach 2 (starting from 0)
    if n == N:
        print_ans()
        return 


    for i in range(1, K+1):
        answer.append(i)
        # If we chose a number above, we should call the next one. 
        choose_k(n+1)
        # If we reach the terminal, we should pop it.
        answer.pop()

    return


choose_k(0)