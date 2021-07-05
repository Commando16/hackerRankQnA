def alternate(s):
    count = dict(Counter(s))
    string = s
    s = set(s)
    c = list(combinations(s, 2))
    print(count)
    print(c)
    lst = []
    for x in c:
        if abs(count[x[0]]-count[x[1]]) in [0, 1]:
            lst.append(x)
    print(lst)
    
    maxx = 0
    for x in lst:
        vals = {x[0]: 0, x[1]: 1}
        switch = 2
        for z in string:
            if z in vals:
                if switch != vals[z]:
                    switch = vals[z]
                else:
                    break
        else:
            if maxx < count[x[0]]+count[x[1]]:
                maxx = count[x[0]]+count[x[1]]
      
    return maxx


## Done
