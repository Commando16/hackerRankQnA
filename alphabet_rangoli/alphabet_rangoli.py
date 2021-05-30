def print_rangoli(size):
    # your code goes here
    pattern_list=[]

    alphabets = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alphabets = alphabets.split(" ")

    pattern_list.append(("-"*((size*2)-2))+alphabets[size-1]+("-"*((size*2)-2)))
    print(pattern_list[0])

    #print(size)
    rowsize = (size*4)-3
    for x in range(size-1, 0, -1):
        s1 = "-".join(alphabets[x-1:size])
        s1 = s1[:-len(s1):-1] + s1
        dashes = rowsize-len(s1)
        #print(rowsize, dashes)
        s1 = ("-"*(dashes//2))+s1+("-"*(dashes//2))
        print(s1)
        pattern_list.append(s1)

    for x in pattern_list[-2::-1]:
        print(x)


##Done
