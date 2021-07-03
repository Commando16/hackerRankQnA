def drawpattern( arr, arrlength, iteration, max_iteration, seedPosition, stem_length, starter=0 ):

    if iteration <= max_iteration:
        
        #steam_loop
        i = starter
        for i in range(starter,starter+stem_length):
            arr[i]= arr[i][:seedPosition] + "1" + arr[i][seedPosition+1:]
            #print(i)
            
        i+=1

        shifter = 0 
        while i<(starter+(stem_length*2)):    
            arr[i]= arr[i][:seedPosition-shifter-1] + "1" + arr[i][seedPosition-shifter:seedPosition+shifter+1] + "1" + arr[i][seedPosition+shifter+2:] 
            #print(i,starter+stem_length,shifter, stem_length,seedPosition)
            shifter+=1
            i+=1

            
        
        seed_left_pos = seedPosition-shifter
        seed_right_pos = seedPosition+shifter
       
        #print("left seed position=", seed_left_pos ,"right seed position=" ,seed_right_pos)
        
        
        
        

        #drawleft branch
        
        #print("entered in left")
        drawpattern( arr, arrlength, iteration+1, max_iteration, seed_left_pos, stem_length//2, i)
        
        #drawright branch
        drawpattern( arr, arrlength, iteration+1, max_iteration, seed_right_pos, stem_length//2, i)
        
        
        '''
        #print(arr[0])
        print(len(arr[0]))

        #steam_printing_loop
        for i in range(-1,(-(len(arr))-1),-1):
            print(arr[i])
        '''
        
            
    else:
        '''
        for i in range(-1,(-(len(arr))-1),-1):
            print(arr[i])
        
        '''
        
        '''
        printer(arr)
        '''
        
        b = arr 
        return b

    

   
    

    


grid = []

for x in range(0,63):
    grid.append(("_"*100))


arrlength = 100
iteration = 1
max_iteration = 5
seedPosition = (arrlength//2)-1
stem_length = 16
'''
drawpattern( grid, arrlength, iteration, max_iteration, seedPosition, stem_length)
'''
'''
grid = drawpattern( grid, arrlength, iteration, max_iteration, seedPosition, stem_length)
'''
'''
print( drawpattern( grid, arrlength, iteration, max_iteration, seedPosition, stem_length) )
'''

b = drawpattern( grid, arrlength, iteration, max_iteration, seedPosition, stem_length)

for i in range(-1,(-(len(grid))-1),-1):
            print(grid[i])


