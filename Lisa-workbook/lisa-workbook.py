def workbook(n, k, arr):
    page_list = []

    for x in arr:
        temp = []

        remain = x % k

        if remain > 0:
            
            i = 1
            while i <= x-remain :
                temp.append(i)

                if i%k == 0:
                    page_list.append(temp)
                    temp=[]

                i+=1
            
            while i <= x:
                temp.append(i)
                i+=1
            page_list.append(temp)
        
        else:
            i = 1
            while i <= x-remain :
                temp.append(i)

                if i%k == 0:
                    page_list.append(temp)
                    temp=[]

                i+=1

    print(page_list)

    count = 0
    j = 0

    while j < len(page_list):
        for Y in page_list[j]:        
            if Y == j+1:
                count+=1
        j+=1
    
    return count


# Done
