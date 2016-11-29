#!/bin/python

#a = list(map(int, input().split(' ')))
a = [int(k) for k in input().split(' ')]
b = [int(k) for k in input().split(' ')]

la = len(a)
lb = len(b)
for i in range(lb):
    a.append(-1)
print (a)

for i in range(la):
    a[i+lb] = a[i] 
    a[i] = -1

print(a)

sia = lb
eia = lb + la

sib = 0
eib = lb

index = 0
while sia < eia and sib < eib:
    if (a[sia] < b[sib]):
        a[index] = a[sia]
        sia+=1
    else:
        a[index] = b [sib]
        sib += 1
    index+=1

if sib < eib:
    for i in range (eib - sib):
        a[index] = b[sib]
        sib += 1
        index += 1

print (a)
