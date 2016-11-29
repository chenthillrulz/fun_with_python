#!/bin/python

string = "abcd"
string = [s for s in string]
#print (string)
total = 0

def permutation (result, remaining):
	if len(remaining) == 0:
		print (result)
		global total
		total += 1
	for s in remaining:
		result.append(s)
		
		n_remaining = remaining[:]
		# optimize it to remove from location rather than finding string
		n_remaining.remove(s)
		
		permutation (result, n_remaining)
		result.pop()


permutation([], string)
print (total)	
