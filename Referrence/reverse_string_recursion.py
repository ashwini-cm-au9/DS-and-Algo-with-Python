#reverse of a string(using Recursion)
def solve(st):
    if len(st)==0:
        return ""
    return solve(st[1:])+st[0]
print(solve("abc"))
