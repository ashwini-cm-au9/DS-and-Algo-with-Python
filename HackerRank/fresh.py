def solve(st,idx,res,all):
    if idx==len(st):
        all.append(res[:])
        return all

    if len(res)==len(st):
        all.append(res[:])
        #res.pop()
        return all

    res2=res[:]
    res2.append(st[idx])
    solve(st,idx,res2,all) 

    
    solve(st,idx+1,res,all)

    #return all
    '''def passwordCracker(passwords, loginAttempt,start,end,lis):
    # Write your code here
    if start==len(loginAttempt):
        return lis
    elif end>len(loginAttempt):
        return 1
    if loginAttempt[start:end] in passwords:
        lis.append(loginAttempt[start:end])
        return passwordCracker(passwords,loginAttempt,end,end+1,lis)
    else:
        return passwordCracker(passwords,loginAttempt,start,end+1,lis)'''



if __name__ == "__main__":
    st="abc"
    all=[]
    print(solve(st,0,[],all))

    for i in range(len(all)):
        print(all[i])