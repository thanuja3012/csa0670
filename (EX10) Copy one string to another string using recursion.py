def copy(a,b,index=0):
    if index==len(a):
        return b
    b+=a[index]
    return copy(a,b,index+1)
a="hello world"
b=""
print(copy(a,b))
