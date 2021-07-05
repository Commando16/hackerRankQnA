def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    lower = 1
    upper = 1
    digit = 1
    special = 1
    
    for x in password:
        char_ascii = ord(x)
        
        if char_ascii in range(97,123): # lower case
            lower=0
        elif char_ascii in range(65,91): # upper case
            upper=0
        elif char_ascii in range(48,58): # digit
            digit=0
        elif x in ['!','@','#','$','%','^','&','*','(',')','-','+']: 
            special=0
        
        
    # print(lower, upper, digit, special)
    
    if len(password)>=6:
        return upper+lower+digit+special
        
    else:
        if 6-(len(password)) > (upper+lower+digit+special):
            return  6-(len(password))
        else:
            return (upper+lower+digit+special)

## Done
