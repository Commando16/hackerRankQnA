# Complete the minimumBribes function below.
def minimumBribes(q):
    length_q = len(q)
    arr = []
    for x in range( 1 , length_q+1 ):
        arr.append(x)

    #print(arr)
    #print(q)
    
    
    i = 0

    brib = 0
    

    while i < length_q:
        if q[i] != arr[i]:
            j = i+1
            counter = 1
            while j<length_q:
                #print("if m aaya comparing",q[i], arr[i])
                if counter>2:
                    print("Too chaotic")
                    return

                if q[i] == arr[j]:
                    diff = (j-i)

                    '''
                    if diff>2:
                        flag = 1
                        break
                    '''

                    brib += diff 
                
                    popped_number = arr.pop(j)
                    #print(arr)
                    arr.insert(i,popped_number)
                    break
                    #print(popped_number, i)
                    #print(arr)

                counter+=1
                j+=1
            
        i+=1
    
    #print(arr)
    '''
    if flag == 1:
        print("Too chaotic")
    else: 
        print(brib)
    '''
    print(brib)



# Done
