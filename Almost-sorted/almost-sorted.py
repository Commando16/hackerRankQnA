
def almostSorted(arr):
    defected_order = []

    length_arr = len(arr)

    temp_start = 0
    temp_end = 0

    if length_arr==2:
        print("yes\nswap", 0+1, 1+1)
        return

    # loop for recognising how many defected{not arranged in assending order} area are there and marking their start and end position.......
    i=0
    while i < length_arr-1:
        if arr[i]>arr[i+1]:
            temp_start = i
            j=i+1
            while j < length_arr-1:
                if arr[j]<=arr[j+1]:
                    break
                j+=1
            i = j
            temp_end = i

            defected_order.append([temp_start,temp_end])
        i+=1
        
    # debug print.....printing defected
    print(defected_order)
    

    if len(defected_order)==0:
        print("yes")
    elif len(defected_order)==1:
        # deference of end minus start
        start_index = defected_order[0][0]
        end_index = defected_order[0][1]
        
        if (end_index-start_index) == 1:
            #Possible with swap

            # if the start index is zero we cannot see the comparison from start index-1 to end index+1
            if start_index == 0:  

                if arr[start_index]<arr[end_index]<arr[end_index+1]:
                    print("yes\nswap", start_index+1, end_index+1)
                    return
                else:
                    print("no")
                    return

            elif end_index == length_arr-1:  

                if arr[start_index-1]<arr[start_index]<arr[end_index]:
                    print("yes\nswap", start_index+1, end_index+1)
                    return
                else:
                    print("no")
                    return
            else:
                if arr[start_index-1]<arr[start_index]<arr[end_index]<arr[end_index+1]:
                    print("yes\nswap", start_index+1, end_index+1)
                    return
                else:
                    print("no")
                    return
        else:
            #Possible with reverse
            start_index = defected_order[0][0]
            end_index = defected_order[0][1]

            #i think no need of actuall reversal.....on cheching by assuming that starting index element is now at end index and visa versa....

            # assing the start and end but with opposit indexing as mention in above comment...
            #start_index = defected_order[0][1]
            #end_index = defected_order[0][0]

            if start_index == 0:  

                # starting index represent end index after reversal
                if arr[start_index]<arr[end_index+1]:
                    print("yes\nreverse", start_index+1, end_index+1)
                    return
                else:
                    print("no")
                    return

            elif end_index == length_arr-1:  

                if arr[start_index-1]<arr[end_index]:
                    print("yes\nreverse", start_index+1, end_index+1)
                    return
                else:
                    print("no")
                    return

            else:
                if arr[start_index-1]<arr[end_index]<arr[start_index]<arr[end_index+1]:
                    print("yes\nreverse", start_index+1, end_index+1)
                    return
                else:
                    print("no")
                    return
            
    else:
        print("no")



## Done

