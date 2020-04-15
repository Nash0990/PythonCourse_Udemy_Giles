def TwoSum(my_list,target):
    output=[]

    for i in range(0,len(my_list)):
        for j in range(1+i,len(my_list)):
            tot=my_list[i]+my_list[j]
            if tot==target:
                output.append(i)
                output.append(j)
                return output
    if len(output)==0:
        output.append(-1)
    return output

def TwoSum2(my_list,target):
    d = {}
    for i in range(len(my_list)):
        if target - my_list[i] in d:
            #print(d)
            return [d[target - my_list[i]],i]
        d[my_list[i]]=i
    return -1
