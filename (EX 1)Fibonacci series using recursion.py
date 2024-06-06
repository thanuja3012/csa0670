def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
a=10
for i in range(a):
    print(fib(i))
