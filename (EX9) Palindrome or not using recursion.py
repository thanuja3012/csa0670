def palindrome(string):
    if string.lower()==string[::-1].lower():
        return True
    else:
        return False
a="women"
if palindrome(a):
    print(True)
else:
    print(False)
