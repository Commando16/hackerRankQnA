def queensAttack(n, k, r_q, c_q, obstacles):
    up = n - r_q
    down = r_q-1
    right = n - c_q
    left = c_q-1
    up_right = min(up, right)
    down_right = min(right,down)
    up_left = min(left,up)
    down_left = min(left,down)
    for i, o in enumerate(obstacles):
        print(abs(o[0]-r_q), abs(o[1]-c_q))
        if abs(o[0]-r_q) == abs(o[1]-c_q):
            if o[1]<c_q and o[0]>r_q:#up_left
                if up_left>abs(o[1]-c_q)-1:
                    up_left = abs(o[1]-c_q)-1
            elif o[1]>c_q and o[0]>r_q:#up_right
                if up_right>abs(o[1]-c_q)-1:
                    up_right = abs(o[1]-c_q)-1
            elif o[1]<c_q and o[0]<r_q:#down_left
                if down_left>abs(o[1]-c_q)-1:
                    down_left = abs(o[1]-c_q)-1
            elif o[1]>c_q and o[0]<r_q:#down_right
                if down_right>abs(o[1]-c_q)-1:
                    down_right = abs(o[1]-c_q)-1

        elif o[0] == r_q or o[1] == c_q:   
            if r_q==o[0] and c_q>o[1]:#left
                left = min(left, abs(c_q-o[1])-1)
            elif r_q==o[0] and c_q<o[1]:#right
                right = min(right, abs(c_q-o[1])-1)
            elif r_q<o[0] and c_q==o[1]:#up
                up = min(up, abs(r_q-o[0])-1)
            elif r_q>o[0] and c_q==o[1]:#down
                down = min(down, abs(r_q-o[0])-1)
            
    return up_left+up_right+down_left+down_right+left+ right+up+down


## done
