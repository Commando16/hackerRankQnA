  #     &    *   ()   !=    &&   @    $


def picker( numbers ):

    catagory=[]
    
    for X in range(0, 100):
        catagory.append([X,0])

##    print(catagory)

    for X in numbers:
        catagory[X][1]+=1

##    print(catagory)
    i=0
    maximum=0

    while i<len(catagory)-1:
        new_sum = catagory[i][1] + catagory[i+1][1]
##        print(new_sum)
        
        if  new_sum > maximum:
            maximum = new_sum
        i+=1

    return maximum
print(picker([9, 5, 6, 2, 3, 1, 7, 8, 5, 2, 6, 4, 7, 1, 3, 6, 9, 8]))
##print(picker([4, 6, 5, 3, 3, 1]))
##print(picker([1, 2, 2, 3, 1, 2]))




########Done
