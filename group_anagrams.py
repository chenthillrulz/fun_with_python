#!/bin/python

array = ["a", "abcd", "az", "bcd", "bcda"]

a = dict()

for w in array:
    key = ''.join(sorted(w))
    print (key)
    if key in a:
        v = a[key]
        v.append(w)
    else:
        v = []
        v.append(w)
        a[key] = v 

for k, v in a.items():
    print (v)
