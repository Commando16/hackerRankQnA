def isValid(s):
    AlphabetGrouping = {'a':0, 'b':0, 'c':0,'d':0,'e':0, 'f':0, 'g':0, 'h':0, 'i':0,'j':0, 'k':0, 'l':0,'m':0,'n':0, 'o':0, 'p':0, 'q':0, 'r':0,'s':0, 't':0, 'u':0, 'v':0,'w':0,'x':0,'y':0,'z':0}


    for x in s:
        AlphabetGrouping[x]+=1

    '''
    for x in AlphabetGrouping:
        print(x, AlphabetGrouping[x])
    '''

    OccurenceGrouping = {}
    for x in AlphabetGrouping:
        if AlphabetGrouping[x] in OccurenceGrouping:
            OccurenceGrouping[AlphabetGrouping[x]]+=1
        else:
            if AlphabetGrouping[x] != 0:
                OccurenceGrouping.update({AlphabetGrouping[x]:1})

    '''
    for x in OccurenceGrouping:
        print(x, OccurenceGrouping[x])
    '''

    if len(OccurenceGrouping)==1:
        return "YES"
    
    elif len(OccurenceGrouping)==2:
        OccurenceGroupinglist = []
        for x in OccurenceGrouping:
            OccurenceGroupinglist.append([x, OccurenceGrouping[x]])
        
        #print(OccurenceGroupinglist)

        base_no_diff = abs(OccurenceGroupinglist[0][0]-OccurenceGroupinglist[1][0])
        #print(base_no_diff)
        
        if base_no_diff == 1:
            '''
            if OccurenceGroupinglist[0][1]==1 and OccurenceGroupinglist[1][1]==1:
                return "YES"
            '''
            min = 0
            if OccurenceGroupinglist[0][1] <= OccurenceGroupinglist[1][1]:
                min = OccurenceGroupinglist[0][1]
            else:
                min = OccurenceGroupinglist[1][1]

            if min == 1:
                return "YES"
            else:
                return "NO"
        
        elif OccurenceGroupinglist[0][0]==1 and OccurenceGroupinglist[0][1]==1:
            return "YES"
            
        elif OccurenceGroupinglist[1][0]==1 and OccurenceGroupinglist[1][1]==1:
            return "YES"

        else:
            return "NO"

    else:
        return "NO"

## Done
