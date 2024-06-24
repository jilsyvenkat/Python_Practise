# def fib(n):
#    if n <= 1:
#        print(n)
#        return n
#    else:
#        return fib(n - 1) + fib(n - 2)

def fib(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n - 1, computed) + fib(n - 2, computed)
    return computed[n]

print(fib(10))

# 0 1 2 3 4 5 6 7   8  9  10
# 0 1 1 2 3 5 8 13 21  34 55

9+8