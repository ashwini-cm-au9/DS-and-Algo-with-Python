#substring of a string
def solve(st,idx,res):
    if idx==len(st):
        print(res)
        return
    solve(st,idx+1,res+st[idx])
    solve(st,idx+1,res)
    
solve("abc",0,"")
