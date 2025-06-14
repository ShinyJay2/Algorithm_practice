expression = input()

# hmm... Let's recurse with with number of alpahbets
# but if we have the same alphabet no need for 1~4, just set it

# Also we need a computing method

unique_chars = sorted(set(char for char in expression if char.isalpha()))
char_dict = dict()

def compute(expression, char_dict):

    result = 0
    i = 0

    # Assuming we have a completed char_dict...
    for elem in expression:
        if elem.isalpha():
            if i == 0:
                result += char_dict[elem]

            elif expression[i - 1] == "+":
                result += char_dict[elem]
            elif expression[i - 1] == "-":
                result -= char_dict[elem]
            elif expression[i - 1] == "*":
                result *= char_dict[elem]
        i += 1

    return result

# We need char_list = [b, a, b, c, b] but in numbers
# Now we need to make somekind of dict, maybe only assign keys first


# Maybe we will just decide the params in the dfs first, before writing the compute function
# idx would be the first char


best = float('-inf')

def dfs(idx):

    global best

    if idx == len(unique_chars):
        cur_value = compute(expression, char_dict)
        best = max(best, cur_value)
        return 

    # Now we need to decide values
    char = unique_chars[idx]
    for i in range(1, 5):
        char_dict[char] = i
        dfs(idx + 1)

dfs(0)
print(best)






