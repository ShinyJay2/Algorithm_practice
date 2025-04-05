N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

result = []

for elem, direction in zip(num, command):

    if direction == "push_back":
        result.append(elem)
    elif direction == "pop_back":
        result.pop()
    elif direction == "size":
        print(len(result))
    elif direction == "get":
        print(result[elem-1])



