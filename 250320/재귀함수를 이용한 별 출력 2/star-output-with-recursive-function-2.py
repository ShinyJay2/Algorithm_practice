n = int(input())

def function1(n):

    if n == 0:
        return

    print("* " * n)
    function1(n - 1)
    print("* " * n)


    
function1(n)