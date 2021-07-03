def move_counter_at_direction( blocks, Q_pos_x, Q_pos_y, X_move, Y_move, restricted_blocks ):
##    Q_pos_x = Q_pos_x-1
##    Q_pos_y = Q_pos_y-1

    total_move = 0

    
    while True:
        Q_pos_x = Q_pos_x + X_move
        Q_pos_y = Q_pos_y + Y_move

        if Q_pos_x <= 0 or Q_pos_y <= 0 :
            break
        
        elif Q_pos_x > blocks or Q_pos_y > blocks :
            break

        elif [Q_pos_x,Q_pos_y] in restricted_blocks:
            break

        else:
##            Q_pos_x = Q_pos_x + X_move
##            Q_pos_y = Q_pos_y + Y_move
##            print("else")
            total_move+=1

        print( Q_pos_x, Q_pos_y)

    return total_move

def total_move_counter(  blocks, Q_pos_x, Q_pos_y, restricted_blocks ):
    sum_total_move = 0

    for X in range(-1,2):
        for Y in range(-1,2):

            if X==0 and Y==0:
                continue
            else:
                temp = move_counter_at_direction( blocks, Q_pos_x, Q_pos_y, X, Y, restricted_blocks )
                sum_total_move += temp
##            print(X,Y)
    return sum_total_move
    

                
       
print(total_move_counter(8, 1, 8, [[3,8], [3,6], [1,6]]))


##########  Done
