def solve(sum,pow,idx,res,cnt,path):
    if idx**pow==sum:
        res.append(idx**pow)
        path.append(res[:])
        cnt+=1
        return 1
    if sum<idx**pow:
        return 0

    if sum>idx**pow:
        res2=res[:]
        res2.append(idx**pow)
        return solve(sum-(idx**pow),pow,idx+1,res2,cnt,path) + solve(sum,pow,idx+1,res,cnt,path)

if __name__ == "__main__":
    res=[]
    path=[]
    cnt=0
    print(solve(100,2,1,res,cnt,path))
    print(path)