def serviceLane(widths, cases):
    result = []
    #print(widths)
    
    for caseiterator in cases:
        #print(caseiterator)
        #print(min(widths[ caseiterator[0]: (caseiterator[1]+1) ]))
        result.append(min(widths[ caseiterator[0]: (caseiterator[1]+1) ]))
    
    return result



##Done
