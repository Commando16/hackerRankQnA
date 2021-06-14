def checkMagazine(magazine, note):
    M = Counter(magazine)
    N = Counter(note)
    
    if len(N-M) == 0:
        print("Yes")
    else:
        print("No")



## Done
