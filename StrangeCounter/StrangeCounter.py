def strangeCounter(t):
    counter = 1
    strange_counter = 3
    
    while counter+strange_counter <= t:
        counter = counter+strange_counter
        strange_counter = strange_counter*2
        
    diff = t - counter 
    
    return strange_counter-diff



## Done
