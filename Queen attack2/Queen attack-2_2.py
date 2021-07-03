##def move_counter_at_direction( blocks, Q_pos_x, Q_pos_y, X_move, Y_move, restricted_blocks ):
##
##    total_move = 0
##    
####    while True:
####        Q_pos_x = Q_pos_x + X_move
####        Q_pos_y = Q_pos_y + Y_move
####
####        if Q_pos_x <= 0 or Q_pos_y <= 0 :
####            break
####        
####        elif Q_pos_x > blocks or Q_pos_y > blocks :
####            break
####
####        elif [Q_pos_x,Q_pos_y] in restricted_blocks:
####            break
####
####        else:
####            total_move+=1
####
####        print( Q_pos_x, Q_pos_y)
####
####    return total_move
####    restrict=[]
####    
####    for X in restricted_blocks:
####        if X[0]==Q_pos_x or  


def move_left( blocks, Q_pos_x, Q_pos_y, restricted_blocks ):
    resctrict=0
    for X in restricted_blocks:
        if X[0] == Q_pos_x and X[1] == Q_pos_y:
            print("left obstecle occure at",X)
            resctrict=[X[0],X[1]]
            break

    for X in restricted_blocks:
        if X[]


def move_right( blocks, Q_pos_x, Q_pos_y, restricted_blocks ):
    resctrict=0
    for X in restricted_blocks:
        if X[1] == Q_pos_y:
            print("right obstecle occure at",X)
            resctrict=[X[0],X[1]]
            break



def total_move_counter(  blocks, Q_pos_x, Q_pos_y, restricted_blocks ):
    sum_total_move = 0

    move_left( blocks, Q_pos_x, Q_pos_y, restricted_blocks )
    move_right( blocks, Q_pos_x, Q_pos_y, restricted_blocks )

                
       
total_move_counter(8, 1, 8, [[3,8], [3,6], [1,6]])


##########  Done
