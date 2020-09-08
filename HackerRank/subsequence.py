def subsequence(st,idx,res,all):
    if idx==len(st):
        all.append(res[:])
        return all

    res.append(st[idx])
    subsequence(st,idx+1,res,all)

    res.pop()
    subsequence(st,idx+1,res,all)

    #return all

if __name__ == "__main__":
    st="abc"
    res=[]
    all=[]
    print(subsequence(st,0,res,all))
    print(all)
    
