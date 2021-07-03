from itertools import permutations
from math import factorial

cars_speed_arr = [10,20,30]
total_cars = len(cars_speed_arr)
pre = permutations(cars_speed_arr)

'''print(pre)'''

group = []

for Single_list in pre:
    length = len(Single_list)
    i = 0

    temp=[Single_list[i]]
    while i < length-1:
        if temp[0]>Single_list[i+1]:
            group.append(temp)
            temp=[Single_list[i+1]]

        else:
            temp.append(Single_list[i+1])

        i+=1
    group.append(temp) 


total_group= len(group)
print(total_group)

'''
for X in group:
    print(X)
'''

print("%.6f" %(total_group/(factorial(total_cars))))















'''
group = []
Single_list = [78, 56, 92, 13]

length = 4
i = 0

temp=[Single_list[i]]
while i < length-1:
    if temp[0]>Single_list[i+1]:
        group.append(temp)
        temp = [Single_list[i+1]]

    else:
        temp.append(Single_list[i+1])

    i += 1
    
group.append(temp)    
'''

