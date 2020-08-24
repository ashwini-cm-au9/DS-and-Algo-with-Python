#sum_target
def coin(lst,idx,target_sum,res):
    if target_sum==0:
        print(res)
        return
    if target_sum<0:
        return
    if idx==len(lst):
        return
    
    res.append(lst[idx])
    target_sum-=lst[idx]
    coin(lst,idx,target_sum,res)

    target_sum+=lst[idx]
    res.pop()
    coin(lst,idx+1,target_sum,res)
    
coin([1,2,5],0,10,[])
