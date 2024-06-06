def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=1
b=3
print(gcd(a,b))
