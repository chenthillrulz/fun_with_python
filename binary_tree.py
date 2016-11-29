#!/bin/python3

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  def addLeft(self, node):
    self.left = node
  def addRight(self, node):
    self.right = node	  

node = Node(1)
n1 = Node (2)
n2 = Node (3)
node.addLeft(n1)
node.addRight(n2)

n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.addLeft(n4)
n4.addLeft(n5)
n1.addRight(n6)
n6.addRight(n7)	

# Find first ancestor of 4 and 7	
a = 4
b = 5
crossed_a = False
crossed_b = False
first_ancestor = None

def postOrder (node):
  global a
  global b
  global first_ancestor
  
  if node is None or first_ancestor:
    return False, False
  
  found_al, found_bl = postOrder(node.left)
  found_ar, found_br = postOrder(node.right)
 
  found_a = True if found_al or found_ar else False
  found_b = True if found_bl or found_br else False 

  if found_a and found_b and first_ancestor == None:
    first_ancestor = node
  
  if node.data == a: found_a = True
  if node.data == b: found_b = True

  return found_a, found_b

    
postOrder(node)
print (first_ancestor.data)
