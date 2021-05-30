def flatlandSpaceStations(n, c):
    print(n)
    c = sorted(c) 
    print(c)
    """
    city_space_station_index = [0]*n
    
    for x in c:
        city_space_station_index[x] = 1
        
    #print(city_space_station_index)
    """

    length = len(c)
    
    if n==length: 
        return 0
    
    elif length > 1:
        # solution for situation having more than one space-station
        distance_between_stations = []
        
        if c[0] != 0:
            distance_between_stations.append(c[0])
    
        i = 0
        while i<length-1:
            print((c[i+1],c[i]))
            distance_between_stations.append(abs(c[i+1]-c[i])//2)
            i+=1
            
        if c[-1] != (length-1):
            distance_between_stations.append((n-1-c[-1]))
            
        print(distance_between_stations)
        print(max(distance_between_stations))
        return (max(distance_between_stations))
        
    else:
        return (max([(c[0]),(n-1-c[0])]))






##Done
