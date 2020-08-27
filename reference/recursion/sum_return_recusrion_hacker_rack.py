def solve(x,N,idx,res):
    if idx**N==x:
        res.append(idx**N)
        return res
    elif idx**N>x:
        return 
    else:
        res2=res[:]
        res2.append(idx**N)
        return solve(x-(idx)**N,N,idx+1,res2) or solve(x,N,idx+1,res)

print(solve(13,2,1,[]))

'''def powerSum(X, N, C):
    if C ** N == X:
        return count + 1
    elif C ** N > X:
        return count + 0
    else:
        return powerSum(X-C**N, N, C + 1) + powerSum(X, N, C + 1)'''  


