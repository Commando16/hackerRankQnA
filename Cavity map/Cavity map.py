def cavityMap(grid):
    length=len(grid[0])
    grid2=[]

    for X in grid:
        temp=[]
        for Y in X:
            temp.append(Y)
        grid2.append(temp)


    i=1
    while i<length-1:
        j=1
        while j<length-1:
            vote=0
            if (grid[i-1][j]!='X') and (grid[i-1][j]<grid[i][j]):
                vote+=1 
            if (grid[i+1][j]!='X') and (grid[i+1][j]<grid[i][j]):
                vote+=1
            if (grid[i][j-1]!='X') and (grid[i][j-1]<grid[i][j]):
                vote+=1
            if (grid[i][j+1]!='X') and (grid[i][j+1]<grid[i][j]):
                vote+=1

            if vote==4:
                grid2[i][j]="X"
            j+=1
        i+=1

    grid3=[]
    for X in grid2:
        temp=""
        for Y in X:
            temp+=Y
        grid3.append(temp)

    return grid3


## done
