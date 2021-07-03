def gridSearch(G, P):
    print(len(G),len(G[0]))
    length_p_row = len(P[0])
    length_p = len(P)
    print(length_p,length_p_row)
    

    iend = len(G)-length_p
    jend = len(G[0])-length_p_row
    print(iend,jend)
    i=0
    while i<=iend:
        j=0
        while j<=jend:
            
            print(G[i][j], end="")
            
            if G[i][j]==P[0][0]:
                rang = j+length_p_row
                if G[i][j:rang] == P[0]:
                    #print(G[i][j:rang])

                    flag = 0
                    x = 1
                    while x < length_p:
                        if G[i+x][j:rang] != P[x]:
                            flag=1
                        x+=1
                    
                    if flag == 0:
                        return "YES"
            
            j+=1
        print("")
        i+=1
    print("")
    return "NO"
