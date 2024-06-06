def lar(a):
    max=a[0]
    for i in range(len(a)):
        if a[i]>max:
            max=a[i]
    return max
a={1,2,3,4,5}
b=list(a)
print(lar(b))
