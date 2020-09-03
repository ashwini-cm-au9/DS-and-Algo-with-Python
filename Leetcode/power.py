#Try to use recursion do Q2.
def powe(n,m):
    if m==0:
        return 1
    return n*powe(n,m-1)
res=powe(2,4)
print(res)
