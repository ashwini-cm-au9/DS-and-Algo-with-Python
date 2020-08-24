#sum of numbers from 1 to n (in recursion)

def solve(n):
    if n<0:
        return 0
    return n+solve(n-1)
print(solve(5))
