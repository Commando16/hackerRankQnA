def theLoveLetterMystery(s):
    length = len(s)
    
    summ = 0
    
    for i in range(0, length//2):
        diff = abs( ord(s[i]) - ord(s[(length-i-1)]) )
        summ += diff
    
    return summ

## Done
