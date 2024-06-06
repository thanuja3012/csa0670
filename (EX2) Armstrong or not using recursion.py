def isarm(num,n):
    if num==0:
        return 0
    else:
        return (num%10)**n+isarm(num//10,n)
def check(num):
    n=len(str(num))
    if num==isarm(num,n):
        return True
    else:
        return False
num=371
if check(num):
    print(f"{num} is armstrong")
else:
    print(f"{num} is not armstrong")
    
