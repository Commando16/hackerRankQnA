from collections import Counter

inp = list(map(lambda x:int(x), input().split(" ")))
n = inp[0]
m = inp[1]

arr = Counter(list(map(lambda x:int(x), input().split(" "))))

A = Counter(list(map(lambda x:int(x), input().split(" "))))
B = Counter(list(map(lambda x:int(x), input().split(" "))))


A = dict(arr & A) 
B = dict(arr & B)
arr = dict(arr)

count = 0
for x in A:
    count+=arr[x]

for x in B:
    count-=arr[x]


print(count)


##Done


