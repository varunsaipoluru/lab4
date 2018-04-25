def memoize(func):
    memo = dict()
    def decorated(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]

    return decorated

@memoize
def fib(n):
    #added for demonstration purposes only - not really needed
    global call_count
    call_count = call_count + 1
    #end demonstration purposes

    if n<=1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

call_count = 0 #added for demonstration purposes only - not really needed
for i in range(100):
    print(fib(i))
