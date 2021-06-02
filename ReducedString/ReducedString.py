def superReducedString(stri):
    i = 0
    
    stri = list(stri)
    while i<len(stri)-1:
        if stri[i]==stri[i+1]:
            del stri[i]
            del stri[i]
            i = 0
            if(len(stri) == 0):
                return "Empty String"
        else:
            i+=1
            
    return "".join(stri)
    
    
##Done
