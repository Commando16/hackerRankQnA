def beautifulTriplets(d, arr):
    # Write your code here
    length = len(arr)
    count = 0
    # while i< length:
        
    for i in range(length):
        for j in range(i+1, length):
            if arr[j]-arr[i] == d:
                for k in range(j+1,length):
                    if arr[k]-arr[j] == d:
                        count+=1
                        break
    
    return count


##Done
