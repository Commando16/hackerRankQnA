def weightedUniformStrings(s, queries):
    length = len(s)
    pos = []
    res = []
    
    weight = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    
    pointed_index = 0
    
    i = 0
    while i<length:
        # print(s[pointed_index],s[i])
        if s[i] != s[pointed_index] :           
            pos.append( (weight[s[pointed_index]], i-pointed_index) )
            pointed_index = i
        else:
            i+=1
            
    pos.append( [weight[s[i-1]], i-pointed_index] )  
    # pos.sort()
    print(pos)
    
    for x in queries:
        for y in pos:
            if x%y[0] == 0 and x/y[0] <= y[1]:
                res.append('Yes')
                break
        else:
            res.append('No')
            
    return res


## Done
