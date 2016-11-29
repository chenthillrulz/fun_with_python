#!/bin/python

source = [1, 2, 3, 4]
aux = []
dest = []

print ("source - " + str(source))
def move_towers (n, source, dest, aux):
	if n == 0:
		return

	move_towers (n-1, source, aux, dest)

	t = source.pop()
	dest.append(t)
	
	move_towers (n-1, aux, dest, source)

move_towers (len(source), source, dest, aux)
print ("destination - " + str(dest))	
