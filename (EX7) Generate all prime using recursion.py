def isprime(num):
    prime=False
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
        else:
            prime=True
    return prime
a=20
for i in range(2,a):
    if isprime(i):
        print(f"{i} is a prime number")
  
