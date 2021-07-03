  #     &    *   ()   !=    &&   @    $


def picker( numbers ):

    catagory=[]
    counter=[]

    for X in numbers:

        if X not in catagory:
            catagory.append(X)
            counter.append(1)
        else:
            counter[catagory.index(X)]+=1
            
##    print(sorted(numbers))
##    print(catagory,"\n",counter)

    C_and_C = sorted(zip(catagory,counter))
##    print(C_and_C)

    maxed_pair=[ -1, -1, -1, -1 ]            ##  both values represent catagory
##    print(maxed_pair)

    i=0 
    while i<(len(C_and_C)-1):
##        print(C_and_C[i],"  ",C_and_C[i+1])
        
        if C_and_C[i+1][0] == C_and_C[i][0]+1 :
##            print("andar aaya")
##            print(maxed_pair) 
            if C_and_C[maxed_pair[0]][1] + C_and_C[maxed_pair[2]][1] < (C_and_C[i][1]) + (C_and_C[i+1][1]):
                maxed_pair[0]= C_and_C[i][0]
                maxed_pair[1]= C_and_C[i][1]
                maxed_pair[2]= C_and_C[i+1][0]
                maxed_pair[3]= C_and_C[i+1][1]
        i+=1

##    print(maxed_pair) 
    if maxed_pair[1] == -1 and maxed_pair[2] == -1:
        return 0
    else:
        return maxed_pair[1]+maxed_pair[3]
        



####print(picker([9, 5, 6, 2, 3, 1, 7, 8, 5, 2, 6, 4, 7, 1, 3, 6, 9, 8]))
##print(picker([4, 6, 5, 3, 3, 1]))
print(picker([1, 2, 2, 3, 1, 2]))




########Test
