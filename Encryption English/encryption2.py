from math import *

def encryption(s):
    length = len(s)
    row = math.floor(math.sqrt(length))
    column = math.ceil(math.sqrt(length))

    res=""

    i = 0
    while i < column :
        j = i
        while j < length:
            #print(s[j],end="")
            res+=s[j]
            j+=column
        #print(" ", end="")
        res+=" "
        i+=1

    return res




## Done
