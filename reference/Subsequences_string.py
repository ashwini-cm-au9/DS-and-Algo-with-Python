def subsequeces(lst,idx,temp,res):
    if idx==len(lst):
        res.append(temp[:])
        return
    
    temp.append(lst[idx])
    subsequeces(lst,idx+1,temp,res)

    temp.pop()
    subsequeces(lst,idx+1,temp,res)

    return res

print(subsequeces([1,2,3],0,[],[]))
