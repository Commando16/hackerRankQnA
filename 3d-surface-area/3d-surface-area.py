def surfaceArea(A):
    total_area = 0
    length_x= len(A[0])
    length_y= len(A)

    i=0
    while i < length_y:
        j=0
        while j<length_x:
            pointed_element_area = 2
            w = j-1
            e = j+1
            n = i-1
            s = i+1

            '''
            w_value = 0
            e_value = 0
            n_value = 0 
            s_value = 0
            '''

            if w == -1 or w== length_x:
                print("west m aaya", i,w)
                pointed_element_area+=(A[i][j])
            else:
                print("west m aaya", i,w)
                if A[i][j] - A[i][w] >= 0:
                    pointed_element_area+=(A[i][j] - A[i][w])

            if e == -1 or e== length_x:
                print("west m aaya", i,e)
                pointed_element_area+=(A[i][j])
            else:
                print("east m aaya", i,e)
                if A[i][j] - A[i][e] >= 0:
                    pointed_element_area+=(A[i][j] - A[i][e])

            if n == -1 or n== length_y:
                print("west m aaya", n,j)
                pointed_element_area+=(A[i][j])
            else:
                print("north m aaya", n,j)
                if A[i][j] - A[n][j] >= 0:
                    pointed_element_area+=(A[i][j] - A[n][j])

            if s == -1 or s== length_y:
                print("west m aaya", s,j)
                pointed_element_area+=(A[i][j])
            else:
                print("south m aaya", s,j)
                if A[i][j] - A[s][j] >= 0:
                    pointed_element_area+=(A[i][j] - A[s][j])

            print(pointed_element_area)
            total_area+=pointed_element_area
            j+=1
        i+=1
    return total_area

## Done

