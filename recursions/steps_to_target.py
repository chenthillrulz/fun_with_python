#!/bin/python3

n = int(input())
steps = [1,2,3]
steps_list = []

def steps_to_target (current_total, path):
	print (current_total)
	global n
	global steps_list
	if current_total == n:
		print (path)
		steps_list.append(path)
		return
	elif current_total > n:
		return

	for s in steps:
		new_list = path[:]
		new_list.append(s)
		steps_to_target	(current_total + s, new_list)

path = []	
steps_to_target(0, path)

print ("Total number to ways to reach " + str(n) + " steps is - " + str(len(steps_list)))	
