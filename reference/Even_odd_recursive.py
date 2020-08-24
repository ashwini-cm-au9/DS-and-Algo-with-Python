#python-program-determine-even-odd-recursively
def solve(num):
    if num-2==0:
        return True
    else:
        return False
    return solve(num-2)

if(solve(int(input()))==True):
    print("even")
else:
    print("odd")
