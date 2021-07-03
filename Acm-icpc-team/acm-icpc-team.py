def acmTeam(topic):
    length = len(topic)
    maxx = [0,0]
    
    i = 0
    while i<length-1:
        j = i + 1
        while j<length:
            num1 = int(topic[i], 2)
            num2 = int(topic[j], 2)
            # print(num1, num2)
            knowledge = bin(num1|num2)[2:]
            total_knowledge = dict(Counter(knowledge))["1"]
            
            # print(f"{topic[i]}\n{topic[j]}\n{knowledge}\n{total_knowledge}", end="\n\n")
            
            if maxx[0] < total_knowledge:
                maxx[0], maxx[1] = total_knowledge, 1
            
            elif maxx[0] == total_knowledge:
                maxx[1]+=1

            j+=1
        i+=1
    
    return maxx


## Done
