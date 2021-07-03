def pickingNumbers(a):
    # Write your code here
    arr = [0]*101
    print(len(arr))
    for x in a:
        arr[x]+=1
    
    i=0
    count=0
    while i<=100:
        #print(i, arr[i])
        if i==100:
            if arr[99]+arr[100] > count:
                count=arr[99]+arr[100]
                
        
        elif arr[i]+arr[i+1] > count:
            count=arr[i]+arr[i+1]

        i+=1
    return count
