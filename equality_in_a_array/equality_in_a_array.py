def equalizeArray(arr):
    catagory=[]
    

    for X in arr:
        i=0
        flag=0
        while i<len( catagory ):
            flag=0
            if catagory[i][0] == X:
                catagory[i][1]+=1
                flag=1
                break; 
            i+=1

        if flag is 0:
            temp=[X,1]
            catagory.append(temp)
           
##    print(catagory)
    maxi=0
    for X in catagory:
        if X[1]>maxi:
            maxi=X[1]

##    print(maxi)

    return len(arr)-maxi

    
print(equalizeArray([3,3,2,1,3]))


########    Done
