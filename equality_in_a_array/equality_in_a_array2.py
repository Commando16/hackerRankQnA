def equalizeArray(arr):

    counter = [0]*101
    for x in arr:
        counter[x]+=1
    print(counter)

    
    maxi = max(filter(lambda x:x!=0, counter))

    return len(arr)- maxi

########    Done
