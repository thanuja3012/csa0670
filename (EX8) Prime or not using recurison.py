def isprime(n):
    prime=False
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
        else:
            prime=True
    return prime
a=11
if isprime(a):
    print(f"{a} is a prime number")
else:
    print(f"{a} is not a prime")
