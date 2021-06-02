def happyLadybugs(stri):
    length = 0
    pos = []
    pos_pointer = 0

    for i,x in enumerate(stri):
        #print(i,x)
        if x != stri[pos_pointer]:
            pos.append(i)
            pos_pointer = i

        length+=1
        
    #print(pos)

    #print(stri) 
    occurance = {}
    prev = 0

    for x in pos:
        #print(prev,x)
        if stri[prev] not in occurance:
            occurance.update({stri[prev]:[(x+1)-(prev+1)]})  
        else:
            occurance[stri[prev]].append((x+1)-(prev+1))
        prev = x


    if stri[prev] not in occurance:
        occurance.update({stri[prev]:[(length)-(prev)]})  
    else:
        occurance[stri[prev]].append((length)-(prev))

    print(occurance)


    if '_' in occurance:
        print("_ wala if chala")
        for x in occurance:
            if sum(occurance[x])<2 and x != '_':
                return "NO"
        return "YES"
    else:
        for x in occurance:
            for y in occurance[x]:
                if y<2:
                    #print(x)
                    return "NO"    
        return "YES"



## Done
