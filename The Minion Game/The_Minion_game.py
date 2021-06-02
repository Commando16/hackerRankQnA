def minion_game( orignal_word ):
    length_str = len(orignal_word)

    S=0
    K=0

    for i, x in enumerate(orignal_word):
        
        if x in ["A","a","E","e","I","i","O","o","U","u"]: 
            K+= (length_str-i)
        else:
            S+= (length_str-i)


    if(S > K):
        print("Stuart", S)
    elif(S < K):
        print("Kevin", K)
    else:
        print("Draw")


## Done
