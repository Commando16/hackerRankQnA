def flippingBits(n):
    #print(n)
    binary = bin(n)
    binary = binary[2:] 
    #print( len(binary) )
    
    if len(binary) < 32:
        binary = ((32-len(binary))*'0')+binary
        #print(binary)
        
    binary2 =""
    for index, x in enumerate(binary):
        if x == '0':
            binary2+='1'
        else:
            binary2+='0'
    
    #print(binary2)                
    #print(int(binary2,2))
    
    return (int(binary2,2))


##  Done
