def hackerrankInString(s):
    desired = 'hackerrank'
    check = 0
    
    for i in s:
        if i == desired[check]:
            check+=1
            if check == len(desired):
                return 'YES'
    return 'NO'


## Done
