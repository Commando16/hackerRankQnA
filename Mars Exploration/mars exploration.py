def marsExploration(s):
    count = 0
    st = "SOS"
    
    i = 0
    for x in s:
        # print(st[i], end=" ")
        if x != st[i]:
            count+=1
        
        i+=1
        i = i%3
    
    return count

## Done
