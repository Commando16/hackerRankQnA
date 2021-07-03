def pattern(row, column): 
    mid_row = row//2
    three_pattern_multiplier= 1

    pattern_list = [] 

    for i in range(1,(mid_row)+1):
        total_dash_1 = column-(3*three_pattern_multiplier)
        pattern_string = "-"*(total_dash_1//2) + ".|."*(three_pattern_multiplier)             +"-"*(total_dash_1//2) 

        print(pattern_string)
        pattern_list.append(pattern_string)

        three_pattern_multiplier+=2

    total_dash_2 = column-7
    print("-"*(total_dash_2//2) + "WELCOME" + "-"*(total_dash_2//2))

    i=len(pattern_list)-1
    while(i>=0):
        print(pattern_list[i])
        i-=1

inp = input().split(" ") #input

r = int(inp[0])
c = int(inp[1])


pattern(r,c)


## Done
